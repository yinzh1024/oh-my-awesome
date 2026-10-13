from pathlib import Path

from oh_my_awesome.classifier import Classification
from oh_my_awesome.config import Category, Config
from oh_my_awesome.models import StarredRepo
from oh_my_awesome.render import (
    BEGIN_MARK,
    END_MARK,
    format_stars,
    render_nav,
    slugify,
    update_readme,
)


def make_config() -> Config:
    return Config(
        title="t",
        sort_by="stars",
        categories=[Category(name="AI / LLM", description="大模型", topics=["llm"])],
        overrides={},
        exclude=[],
    )


def sample() -> Classification:
    repo = StarredRepo(
        full_name="a/b",
        html_url="https://github.com/a/b",
        description="desc\nline2",
        stars=12345,
        language="Python",
        topics=["llm"],
    )
    return Classification(groups={"AI / LLM": [repo], "未分类": []})


def test_format_stars():
    assert format_stars(999) == "999"
    assert format_stars(1234) == "1.2k"
    assert format_stars(1000) == "1k"
    assert format_stars(2_500_000) == "2.5m"


def test_slugify_matches_github():
    assert slugify("AI / LLM") == "ai--llm"
    assert slugify("前端与 Web") == "前端与-web"
    assert slugify("C++ & Rust") == "c--rust"
    assert slugify("  spaced  ") == "spaced"


def test_render_nav_contains_toc_and_entries():
    nav = render_nav(make_config(), sample(), fetched_at="2026-01-01 00:00 UTC")
    assert nav.startswith(BEGIN_MARK) and nav.endswith(END_MARK)
    assert "- [AI / LLM](#ai--llm) (1)" in nav
    assert "## AI / LLM" in nav
    assert "- [a/b](https://github.com/a/b) `★12.3k` - desc line2 · Python" in nav
    assert "共 **1** 个项目" in nav


def test_update_readme_preserves_head_and_is_idempotent(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text(
        f"MY HEADER\n\n{BEGIN_MARK}\nold stuff\n{END_MARK}\n\nFOOTER\n",
        encoding="utf-8",
    )
    nav = render_nav(make_config(), sample())
    assert update_readme(readme, nav) is True
    content = readme.read_text(encoding="utf-8")
    assert content.startswith("MY HEADER")
    assert "FOOTER" in content
    assert "old stuff" not in content
    assert update_readme(readme, nav) is False  # idempotent


def test_update_readme_appends_when_markers_missing(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("# Title\n", encoding="utf-8")
    nav = render_nav(make_config(), sample())
    assert update_readme(readme, nav) is True
    assert BEGIN_MARK in readme.read_text(encoding="utf-8")
