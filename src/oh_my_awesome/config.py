from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

SORT_FIELDS = ("stars", "starred_at")
LLM_SOURCES = ("description", "readme")


class ConfigError(Exception):
    pass


@dataclass
class LLMConfig:
    enabled: bool = False
    base_url: str = "https://api.deepseek.com"
    model: str = "deepseek-flash"
    api_key_env: str = "DEEPSEEK_API_KEY"
    source: str = "description"
    max_readme_chars: int = 1500
    max_per_run: int = 60
    concurrency: int = 5
    keep_original: bool = False
    extra_body: dict = field(default_factory=dict)


@dataclass
class Category:
    name: str
    description: str = ""
    topics: list[str] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    repos: list[str] = field(default_factory=list)
    name_patterns: list[str] = field(default_factory=list)


@dataclass
class Config:
    title: str
    sort_by: str
    categories: list[Category]
    overrides: dict[str, str]
    exclude: list[str]
    llm: LLMConfig = field(default_factory=LLMConfig)

    @property
    def category_names(self) -> list[str]:
        return [c.name for c in self.categories]


def load_config(path: Path) -> Config:
    if not path.exists():
        raise ConfigError(f"config file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"config must be a mapping: {path}")

    sort_by = data.get("sort_by", "stars")
    if sort_by not in SORT_FIELDS:
        raise ConfigError(f"sort_by must be one of {SORT_FIELDS}, got {sort_by!r}")

    categories: list[Category] = []
    for i, raw in enumerate(data.get("categories") or []):
        if not isinstance(raw, dict) or not raw.get("name"):
            raise ConfigError(f"categories[{i}] must be a mapping with a name")
        categories.append(
            Category(
                name=str(raw["name"]),
                description=str(raw.get("description") or ""),
                topics=[str(t).lower() for t in raw.get("topics") or []],
                languages=[str(lang) for lang in raw.get("languages") or []],
                repos=[str(r) for r in raw.get("repos") or []],
                name_patterns=[str(p) for p in raw.get("name_patterns") or []],
            )
        )

    names = [c.name for c in categories]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise ConfigError(f"duplicate category names: {sorted(dupes)}")

    overrides = {str(k): str(v) for k, v in (data.get("overrides") or {}).items()}
    for repo, cat in overrides.items():
        if cat not in names:
            raise ConfigError(f"overrides[{repo!r}] points to unknown category {cat!r}")

    raw_llm = data.get("llm") or {}
    if not isinstance(raw_llm, dict):
        raise ConfigError("llm must be a mapping")
    llm = LLMConfig(
        enabled=bool(raw_llm.get("enabled", False)),
        base_url=str(raw_llm.get("base_url", LLMConfig.base_url)),
        model=str(raw_llm.get("model", LLMConfig.model)),
        api_key_env=str(raw_llm.get("api_key_env", LLMConfig.api_key_env)),
        source=str(raw_llm.get("source", LLMConfig.source)),
        max_readme_chars=int(raw_llm.get("max_readme_chars", LLMConfig.max_readme_chars)),
        max_per_run=int(raw_llm.get("max_per_run", LLMConfig.max_per_run)),
        concurrency=int(raw_llm.get("concurrency", LLMConfig.concurrency)),
        keep_original=bool(raw_llm.get("keep_original", False)),
        extra_body=dict(raw_llm.get("extra_body") or {}),
    )
    if llm.source not in LLM_SOURCES:
        raise ConfigError(f"llm.source must be one of {LLM_SOURCES}, got {llm.source!r}")

    return Config(
        title=str(data.get("title", "oh-my-awesome")),
        sort_by=sort_by,
        categories=categories,
        overrides=overrides,
        exclude=[str(r) for r in data.get("exclude") or []],
        llm=llm,
    )
