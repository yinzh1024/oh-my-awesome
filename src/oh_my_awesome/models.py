from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class StarredRepo:
    full_name: str
    html_url: str
    description: str = ""
    stars: int = 0
    language: str = ""
    topics: list[str] = field(default_factory=list)
    starred_at: str = ""
    archived: bool = False
    fork: bool = False
    homepage: str = ""

    @property
    def owner(self) -> str:
        return self.full_name.split("/", 1)[0]

    @property
    def name(self) -> str:
        return self.full_name.split("/", 1)[-1]
