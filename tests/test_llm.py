from pathlib import Path

from oh_my_awesome.config import LLMConfig
from oh_my_awesome.llm import (
    SummaryEntry,
    build_user_prompt,
    load_summaries,
    sanitize,
    source_hash,
    summarize_repos,
)
from oh_my_awesome.models import StarredRepo


def repo(name: str, stars: int = 100, description: str = "a tool") -> StarredRepo:
    return StarredRepo(
        full_name=name,
        html_url=f"https://github.com/{name}",
        stars=stars,
        description=description,
        topics=["llm"],
        language="Python",
    )


def test_sanitize():
    assert sanitize("“一个工具。”\n第二行") == "一个工具"
    assert sanitize("  plain text  ") == "plain text"
    assert sanitize("") == ""


def test_source_hash_depends_on_source_and_description():
    r = repo("a/b")
    assert source_hash(r, "description") != source_hash(r, "readme")
    assert source_hash(r, "description") == source_hash(repo("a/b"), "description")
    assert source_hash(r, "description") != source_hash(
        repo("a/b", description="other"), "description"
    )


def test_build_user_prompt():
    prompt = build_user_prompt(repo("a/b"), "readme excerpt here")
    assert "项目：a/b" in prompt
    assert "描述：a tool" in prompt
    assert "Topics：llm" in prompt
    assert "主要语言：Python" in prompt
    assert "readme excerpt here" in prompt


def test_summarize_incremental_and_caps(tmp_path: Path, monkeypatch):
    store_path = tmp_path / "summaries.json"
    root = tmp_path
    (root / ".env").write_text("TEST_KEY=secret\n", encoding="utf-8")

    repos = [
        repo("a/one", stars=10),
        repo("a/two", stars=20),
        repo("a/three", stars=30, description="new desc"),
    ]
    # pre-existing: a/one fresh, a/two stale (hash mismatch), manual protected
    from oh_my_awesome.llm import source_hash as sh

    save = {
        "a/one": SummaryEntry(summary="旧摘要", hash=sh(repos[0], "description"), model="m"),
        "a/two": SummaryEntry(summary="过期", hash="stale", model="m"),
        "a/three": SummaryEntry(summary="手改", hash="stale", model="m", manual=True),
    }
    from oh_my_awesome.llm import save_summaries

    save_summaries(store_path, save)

    calls: list[str] = []
    monkeypatch.setattr(
        "oh_my_awesome.llm._chat",
        lambda cfg, key, prompt, session: calls.append(prompt) or "生成的摘要",
    )

    cfg = LLMConfig(api_key_env="TEST_KEY", max_per_run=60, concurrency=1)
    store, n = summarize_repos(repos, cfg, store_path, root=root, quiet=True)
    # only a/two (stale) regenerated; a/one fresh; a/three manual protected
    assert n == 1
    assert store["a/two"].summary == "生成的摘要"
    assert store["a/one"].summary == "旧摘要"
    assert store["a/three"].summary == "手改"
    assert len(calls) == 1

    # force regenerates non-manual entries only
    calls.clear()
    store, n = summarize_repos(repos, cfg, store_path, root=root, force=True, quiet=True)
    assert n == 2  # a/three is manual
    assert store["a/three"].summary == "手改"

    # second run: everything up to date
    calls.clear()
    store, n = summarize_repos(repos, cfg, store_path, root=root, quiet=True)
    assert n == 0


def test_summarize_max_per_run_prefers_high_stars(tmp_path: Path, monkeypatch):
    store_path = tmp_path / "summaries.json"
    (tmp_path / ".env").write_text("TEST_KEY=secret\n", encoding="utf-8")
    repos = [repo("a/low", stars=1), repo("a/mid", stars=50), repo("a/high", stars=900)]
    monkeypatch.setattr(
        "oh_my_awesome.llm._chat",
        lambda cfg, key, prompt, session: "s",
    )
    cfg = LLMConfig(api_key_env="TEST_KEY", max_per_run=1, concurrency=1)
    store, n = summarize_repos(repos, cfg, store_path, root=tmp_path, quiet=True)
    assert n == 1
    assert store["a/high"].summary == "s"
    assert "a/mid" not in store and "a/low" not in store


def test_summarize_missing_key_warns_and_keeps_store(tmp_path: Path):
    store_path = tmp_path / "summaries.json"
    save = {"a/b": SummaryEntry(summary="x", hash="h", model="m")}
    from oh_my_awesome.llm import save_summaries

    save_summaries(store_path, save)
    cfg = LLMConfig(api_key_env="NO_SUCH_KEY")
    store, n = summarize_repos([repo("a/b")], cfg, store_path, root=tmp_path, quiet=True)
    assert n == 0
    assert load_summaries(store_path)["a/b"].summary == "x"


def test_summarize_limit_and_only(tmp_path: Path, monkeypatch):
    store_path = tmp_path / "summaries.json"
    (tmp_path / ".env").write_text("TEST_KEY=secret\n", encoding="utf-8")
    repos = [
        repo("gh/high", stars=300),
        repo("gh/low", stars=5),
        repo("other/x", stars=999),
    ]
    calls: list[str] = []
    monkeypatch.setattr(
        "oh_my_awesome.llm._chat",
        lambda cfg, key, prompt, session: calls.append(prompt) or "s",
    )
    cfg = LLMConfig(api_key_env="TEST_KEY", concurrency=1)
    store, n = summarize_repos(
        repos, cfg, store_path, root=tmp_path, limit=1, only="gh/", quiet=True
    )
    assert n == 1
    assert "gh/high" in store and "gh/low" not in store and "other/x" not in store
