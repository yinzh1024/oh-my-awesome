from pathlib import Path

from oh_my_awesome.classifier import UNCATEGORIZED, classify
from oh_my_awesome.config import Category, ConfigError, load_config
from oh_my_awesome.models import StarredRepo


def repo(name, **kw) -> StarredRepo:
    defaults = dict(full_name=name, html_url=f"https://github.com/{name}", stars=100, topics=[])
    defaults.update(kw)
    return StarredRepo(**defaults)


def make_config(**kw) -> "object":
    from oh_my_awesome.config import Config

    defaults = dict(
        title="t",
        sort_by="stars",
        categories=[
            Category(name="AI", topics=["llm", "ai"], name_patterns=["^awesome[-_]"]),
            Category(name="前端", topics=["react"], languages=["TypeScript"]),
            Category(name="系统", topics=["linux"], languages=["C"]),
        ],
        overrides={"me/forced": "前端"},
        exclude=["me/junk"],
    )
    defaults.update(kw)
    return Config(**defaults)


def test_override_and_exclude():
    cfg = make_config()
    repos = [
        repo("me/forced", topics=["llm"]),
        repo("me/junk", topics=["react"]),
    ]
    res = classify(repos, cfg)
    assert [r.full_name for r in res.groups["前端"]] == ["me/forced"]
    assert res.skipped == ["me/junk"]
    assert UNCATEGORIZED not in res.groups or not res.groups.get(UNCATEGORIZED)


def test_topic_exact_and_token_match():
    cfg = make_config()
    repos = [
        repo("a/llm-tool", topics=["llm"]),
        repo("b/mcp-server", topics=["mcp"]),  # token 'mcp' not present, but 'llm' len>=3
        repo("c/ai-powered", topics=["ai-powered"]),  # 'ai' is <3 chars -> no token match
        repo("d/react-app", topics=["react-dom"]),  # token match on 'react'
    ]
    res = classify(repos, cfg)
    assert [r.full_name for r in res.groups["AI"]] == ["a/llm-tool"]
    assert [r.full_name for r in res.groups["前端"]] == ["d/react-app"]
    assert [r.full_name for r in res.groups[UNCATEGORIZED]] == ["b/mcp-server", "c/ai-powered"]


def test_name_pattern_before_topics():
    cfg = make_config()
    repos = [repo("me/awesome-linux", topics=["linux"])]
    res = classify(repos, cfg)
    assert [r.full_name for r in res.groups["AI"]] == ["me/awesome-linux"]


def test_language_fallback_and_sort():
    cfg = make_config(sort_by="starred_at")
    repos = [
        repo("a/old", language="C", starred_at="2020-01-01T00:00:00Z"),
        repo("b/new", language="C", starred_at="2024-01-01T00:00:00Z"),
        repo("c/ts", language="TypeScript"),
    ]
    res = classify(repos, cfg)
    assert [r.full_name for r in res.groups["系统"]] == ["b/new", "a/old"]
    assert [r.full_name for r in res.groups["前端"]] == ["c/ts"]


def test_load_config_errors(tmp_path: Path):
    bad = tmp_path / "config.yaml"
    bad.write_text("categories:\n  - name: A\n  - name: A\n", encoding="utf-8")
    try:
        load_config(bad)
        raise AssertionError("expected ConfigError")
    except ConfigError:
        pass

    bad.write_text("categories:\n  - name: A\noverrides:\n  x/y: B\n", encoding="utf-8")
    try:
        load_config(bad)
        raise AssertionError("expected ConfigError")
    except ConfigError:
        pass
