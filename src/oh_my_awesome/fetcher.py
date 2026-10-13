from __future__ import annotations

import json
import os
import time
from pathlib import Path

import requests

from .models import StarredRepo

API_URL = "https://api.github.com/user/starred"
HEADERS_BASE = {
    "Accept": "application/vnd.github.star+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


class FetchError(Exception):
    pass


def load_token(root: Path) -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()
    env_file = root / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            if key.strip() in ("GITHUB_TOKEN", "GH_TOKEN") and value.strip():
                return value.strip()
    raise FetchError(
        "no token found: set GITHUB_TOKEN env var, put GITHUB_TOKEN=... in .env, "
        "or define the STARS_TOKEN repository secret for GitHub Actions"
    )


def _request(session: requests.Session, token: str, page: int) -> list:
    headers = dict(HEADERS_BASE, Authorization=f"Bearer {token}")
    for attempt in range(3):
        resp = session.get(API_URL, headers=headers, params={"per_page": 100, "page": page})
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (403, 429) and resp.headers.get("X-RateLimit-Remaining") == "0":
            reset = int(resp.headers.get("X-RateLimit-Reset", "0"))
            wait = max(reset - time.time(), 0) + 1
            if attempt < 2 and wait < 120:
                time.sleep(wait)
                continue
        if resp.status_code == 401:
            raise FetchError("401 Unauthorized: token is invalid or expired")
        if resp.status_code == 403:
            raise FetchError(
                "403 Forbidden: token lacks permission to read your stars "
                "(classic PAT needs public_repo scope)"
            )
        raise FetchError(f"GitHub API error {resp.status_code}: {resp.text[:200]}")
    raise FetchError("rate limited, giving up")


def _normalize(raw: dict) -> StarredRepo:
    stars = raw.get("stars") if "stars" in raw else raw.get("stargazers_count")
    return StarredRepo(
        full_name=raw.get("full_name", ""),
        html_url=raw.get("html_url", ""),
        description=(raw.get("description") or "").strip(),
        stars=int(stars or 0),
        language=raw.get("language") or "",
        topics=[str(t).lower() for t in raw.get("topics") or []],
        starred_at=raw.get("starred_at") or "",
        archived=bool(raw.get("archived")),
        fork=bool(raw.get("fork")),
        homepage=raw.get("homepage") or "",
    )


def fetch_starred(token: str) -> list[StarredRepo]:
    repos: list[StarredRepo] = []
    session = requests.Session()
    page = 1
    while True:
        batch = _request(session, token, page)
        repos.extend(_normalize(item.get("repo", item)) for item in batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def load_cache(path: Path) -> list[StarredRepo]:
    if not path.exists():
        raise FetchError(f"cache not found: {path} (run `oh-my-awesome sync` first)")
    data = json.loads(path.read_text(encoding="utf-8"))
    return [_normalize(item) for item in data["repos"]]


def save_cache(path: Path, repos: list[StarredRepo]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "repos": [vars(r) for r in repos],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
