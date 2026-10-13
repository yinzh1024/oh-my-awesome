from __future__ import annotations

import re
from dataclasses import dataclass, field

from .config import Config
from .models import StarredRepo

UNCATEGORIZED = "未分类"


@dataclass
class Classification:
    groups: dict[str, list[StarredRepo]] = field(default_factory=dict)
    skipped: list[str] = field(default_factory=list)

    @property
    def uncategorized(self) -> list[StarredRepo]:
        return self.groups.get(UNCATEGORIZED, [])


def _topic_matches(repo_topics: set[str], cat_topics: list[str]) -> bool:
    """Exact match, or dash-token match for category topics of 3+ chars.

    Short topics like `ai` or `c` only match exactly, to avoid false hits
    from compound topics such as `ai-driven` or `c-ares`.
    """
    for cat_topic in cat_topics:
        if cat_topic in repo_topics:
            return True
        if len(cat_topic) < 3:
            continue
        for repo_topic in repo_topics:
            if cat_topic in repo_topic.split("-"):
                return True
    return False


def classify(repos: list[StarredRepo], config: Config) -> Classification:
    overrides = {k.lower(): v for k, v in config.overrides.items()}
    exclude = {r.lower() for r in config.exclude}
    manual: dict[str, str] = {}
    patterns: list[tuple[str, list[re.Pattern[str]]]] = []
    for cat in config.categories:
        for repo in cat.repos:
            manual[repo.lower()] = cat.name
        if cat.name_patterns:
            patterns.append((cat.name, [re.compile(p, re.IGNORECASE) for p in cat.name_patterns]))

    groups: dict[str, list[StarredRepo]] = {c.name: [] for c in config.categories}
    result = Classification(groups=groups)

    for repo in repos:
        key = repo.full_name.lower()
        if key in exclude:
            result.skipped.append(repo.full_name)
            continue

        target = overrides.get(key) or manual.get(key)

        if target is None:
            for name, regs in patterns:
                if any(r.search(repo.name) for r in regs):
                    target = name
                    break

        if target is None:
            repo_topics = set(repo.topics)
            for cat in config.categories:
                if _topic_matches(repo_topics, cat.topics):
                    target = cat.name
                    break

        if target is None:
            for cat in config.categories:
                if repo.language and repo.language in cat.languages:
                    target = cat.name
                    break

        if target is None:
            target = UNCATEGORIZED
        groups.setdefault(target, []).append(repo)

    for members in groups.values():
        _sort_members(members, config.sort_by)
    if UNCATEGORIZED in groups:
        _sort_members(groups[UNCATEGORIZED], config.sort_by)

    return result


def _sort_members(members: list[StarredRepo], sort_by: str) -> None:
    if sort_by == "starred_at":
        members.sort(key=lambda r: r.starred_at, reverse=True)
    else:
        members.sort(key=lambda r: r.stars, reverse=True)
