from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from .classifier import UNCATEGORIZED, Classification
from .config import Config
from .models import StarredRepo

BEGIN_MARK = "<!-- oh-my-awesome:begin -->"
END_MARK = "<!-- oh-my-awesome:end -->"


def format_stars(count: int) -> str:
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}m".replace(".0m", "m")
    if count >= 1_000:
        value = f"{count / 1_000:.1f}".rstrip("0").rstrip(".")
        return f"{value}k"
    return str(count)


def slugify(text: str) -> str:
    """Mirror GitHub's heading id: strip punctuation, spaces -> hyphens (no collapsing)."""
    slug = re.sub(r"[^\w\s-]", "", text.lower().strip())
    return slug.replace(" ", "-")


def _entry(repo: StarredRepo, summary: str = "", keep_original: bool = False) -> str:
    parts = [f"- [{repo.full_name}]({repo.html_url}) `★{format_stars(repo.stars)}`"]
    original = repo.description.replace("\n", " ").strip()
    desc = summary.strip() or original
    if desc:
        parts.append(f"- {desc}")
    line = " ".join(parts)
    if keep_original and summary.strip() and original:
        line += f" ｜ {original}"
    if repo.language:
        line += f" · {repo.language}"
    if repo.archived:
        line += " _(archived)_"
    return line


def render_nav(
    config: Config,
    result: Classification,
    fetched_at: str = "",
    summaries: dict[str, str] | None = None,
) -> str:
    summaries = summaries or {}
    keep_original = config.llm.keep_original

    def entry(repo: StarredRepo) -> str:
        return _entry(repo, summaries.get(repo.full_name, ""), keep_original)

    categories = [c for c in config.categories if result.groups.get(c.name)]
    names = [c.name for c in categories]
    total = sum(len(result.groups[n]) for n in names) + len(result.groups.get(UNCATEGORIZED, []))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        BEGIN_MARK,
        f"> 共 **{total}** 个项目 · 最后更新：{now}"
        + (f" · 数据采集：{fetched_at}" if fetched_at else ""),
        "",
        "## 目录",
        "",
    ]
    for cat in categories:
        lines.append(f"- [{cat.name}](#{slugify(cat.name)}) ({len(result.groups[cat.name])})")
    if result.groups.get(UNCATEGORIZED):
        lines.append(
            f"- [{UNCATEGORIZED}](#{slugify(UNCATEGORIZED)}) ({len(result.groups[UNCATEGORIZED])})"
        )
    lines.append("")

    for cat in categories:
        lines.append(f"## {cat.name}")
        lines.append("")
        if cat.description:
            lines.append(f"_{cat.description}_")
            lines.append("")
        lines.extend(entry(r) for r in result.groups[cat.name])
        lines.append("")

    if result.groups.get(UNCATEGORIZED):
        lines.append(f"## {UNCATEGORIZED}")
        lines.append("")
        lines.append("_尚未归类，可在 config.yaml 中通过 topics / overrides 配置分类。_")
        lines.append("")
        lines.extend(entry(r) for r in result.groups[UNCATEGORIZED])
        lines.append("")

    lines.append(END_MARK)
    return "\n".join(lines)


def update_readme(readme_path: Path, nav_block: str) -> bool:
    """Replace the region between markers. Returns True if the file changed."""
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
    else:
        content = f"# {readme_path.stem}\n\n{BEGIN_MARK}\n{END_MARK}\n"

    if BEGIN_MARK in content and END_MARK in content:
        head, _, rest = content.partition(BEGIN_MARK)
        _, _, tail = rest.partition(END_MARK)
        new_content = head + nav_block + tail
    else:
        new_content = content.rstrip("\n") + "\n\n" + nav_block + "\n"

    new_content = new_content.rstrip("\n") + "\n"
    if new_content == content:
        return False
    readme_path.write_text(new_content, encoding="utf-8", newline="\n")
    return True
