from __future__ import annotations

import hashlib
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path

import requests

from .config import LLMConfig
from .fetcher import load_env_value
from .models import StarredRepo

SYSTEM_PROMPT = (
    "你是开源项目导航的编辑。为给定的 GitHub 项目写一句中文简介："
    "不超过 50 个汉字，信息密度高，点明项目是做什么的以及亮点或技术栈；"
    "保留必要的英文专有名词（框架、协议、平台名等）；"
    "不要翻译腔，不要引号，不要以句号结尾，不要复述项目名。"
)


class LLMError(Exception):
    pass


@dataclass
class SummaryEntry:
    summary: str
    hash: str
    model: str = ""
    manual: bool = False


def source_hash(repo: StarredRepo, source: str) -> str:
    payload = f"{source}\n{repo.description}"
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def build_user_prompt(repo: StarredRepo, readme_excerpt: str = "") -> str:
    lines = [f"项目：{repo.full_name}"]
    if repo.description:
        lines.append(f"描述：{repo.description[:500]}")
    if repo.topics:
        lines.append(f"Topics：{', '.join(repo.topics[:8])}")
    if repo.language:
        lines.append(f"主要语言：{repo.language}")
    if readme_excerpt:
        lines.append(f"README 摘录：\n{readme_excerpt}")
    lines.append("输出中文简介：")
    return "\n".join(lines)


def sanitize(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    text = text.splitlines()[0].strip()
    text = text.strip('"""\'\'「」“”').strip()
    text = text.rstrip("。.!！")
    return text[:80]


def fetch_readme_excerpt(full_name: str, gh_token: str, max_chars: int) -> str:
    try:
        resp = requests.get(
            f"https://api.github.com/repos/{full_name}/readme",
            headers={
                "Authorization": f"Bearer {gh_token}",
                "Accept": "application/vnd.github.raw",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.text[:max_chars]
    except requests.RequestException:
        pass
    return ""


def _chat(cfg: LLMConfig, api_key: str, user_prompt: str, session: requests.Session) -> str:
    url = cfg.base_url.rstrip("/") + "/chat/completions"
    body = {
        "model": cfg.model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": 200,
        "temperature": 0.3,
    }
    body.update(cfg.extra_body)
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    last_error = ""
    for attempt in range(3):
        try:
            resp = session.post(url, json=body, headers=headers, timeout=90)
        except requests.RequestException as exc:
            last_error = str(exc)
            time.sleep(2**attempt)
            continue
        if resp.status_code == 200:
            data = resp.json()
            content = data["choices"][0]["message"].get("content") or ""
            return content
        last_error = f"{resp.status_code}: {resp.text[:200]}"
        if resp.status_code in (429, 500, 502, 503, 529) and attempt < 2:
            time.sleep(2 ** (attempt + 1))
            continue
        raise LLMError(last_error)
    raise LLMError(f"request failed after retries ({last_error})")


def load_summaries(path: Path) -> dict[str, SummaryEntry]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        name: SummaryEntry(
            summary=str(entry.get("summary") or ""),
            hash=str(entry.get("hash") or ""),
            model=str(entry.get("model") or ""),
            manual=bool(entry.get("manual")),
        )
        for name, entry in data.items()
    }


def save_summaries(path: Path, entries: dict[str, SummaryEntry]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {name: asdict(entry) for name, entry in sorted(entries.items())}
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n"
    )


def summarize_repos(
    repos: list[StarredRepo],
    cfg: LLMConfig,
    store_path: Path,
    *,
    root: Path,
    gh_token: str | None = None,
    force: bool = False,
    limit: int | None = None,
    only: str | None = None,
    dry_run: bool = False,
    quiet: bool = False,
) -> tuple[dict[str, SummaryEntry], int]:
    """Fill summaries for new/changed repos. Returns (store, n_generated)."""
    store = load_summaries(store_path)

    # drop summaries for repos that are no longer starred (regenerated on re-star)
    current = {r.full_name for r in repos}
    stale = [name for name in store if name not in current]
    if stale:
        for name in stale:
            del store[name]
        if not dry_run:
            save_summaries(store_path, store)
        if not quiet:
            print(f"pruned {len(stale)} summaries no longer starred")

    api_key = load_env_value(root, cfg.api_key_env)
    if not api_key:
        if not quiet:
            print(f"warning: {cfg.api_key_env} not set, skipping summaries")
        return store, 0

    candidates = [r for r in repos if only is None or r.full_name.lower().startswith(only.lower())]
    pending: list[tuple[StarredRepo, str]] = []
    for repo in candidates:
        entry = store.get(repo.full_name)
        if entry and entry.manual:
            continue
        digest = source_hash(repo, cfg.source)
        if entry and not force and entry.hash == digest and entry.summary:
            continue
        pending.append((repo, digest))

    pending.sort(key=lambda item: item[0].stars, reverse=True)
    cap = limit if limit is not None else cfg.max_per_run
    if cap > 0:
        pending = pending[:cap]
    if not pending:
        if not quiet:
            print("summaries up to date")
        return store, 0

    if not quiet:
        print(f"summarizing {len(pending)} repos (source={cfg.source}, model={cfg.model})")

    session = requests.Session()
    generated = 0
    failed = 0

    def work(item: tuple[StarredRepo, str]) -> tuple[str, SummaryEntry]:
        repo, digest = item
        excerpt = ""
        if cfg.source == "readme" and gh_token:
            excerpt = fetch_readme_excerpt(repo.full_name, gh_token, cfg.max_readme_chars)
        text = sanitize(_chat(cfg, api_key, build_user_prompt(repo, excerpt), session))
        return repo.full_name, SummaryEntry(summary=text, hash=digest, model=cfg.model)

    with ThreadPoolExecutor(max_workers=max(cfg.concurrency, 1)) as pool:
        futures = {pool.submit(work, item): item for item in pending}
        for future in as_completed(futures):
            repo, digest = futures[future]
            try:
                name, entry = future.result()
                if not entry.summary:
                    raise LLMError("empty summary")
                if dry_run:
                    print(f"  [dry-run] {name}: {entry.summary}")
                else:
                    store[name] = entry
                generated += 1
            except Exception as exc:  # noqa: BLE001 - keep going per repo
                failed += 1
                if not quiet:
                    print(f"  skip {repo.full_name}: {exc}")

    if not dry_run and generated:
        save_summaries(store_path, store)
    if not quiet:
        print(f"generated={generated} failed={failed} store={len(store)}")
    return store, generated
