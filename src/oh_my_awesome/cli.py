from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from .classifier import UNCATEGORIZED, classify
from .config import ConfigError, load_config
from .fetcher import FetchError, fetch_starred, load_cache, load_token, save_cache
from .gitutils import commit_and_push
from .models import StarredRepo
from .render import render_nav, update_readme


def _paths(args: argparse.Namespace) -> tuple[Path, Path, Path, Path]:
    root = Path(args.root).resolve()
    config_path = Path(args.config) if args.config else root / "config.yaml"
    readme_path = Path(args.readme) if args.readme else root / "README.md"
    cache_path = root / ".cache" / "stars.json"
    return root, config_path, readme_path, cache_path


def _load_repos(
    args: argparse.Namespace, root: Path, cache_path: Path
) -> tuple[list[StarredRepo], str]:
    """Returns (repos, fetched_at_label)."""
    if args.offline:
        return load_cache(cache_path), "缓存"
    repos = fetch_starred(load_token(root))
    save_cache(cache_path, repos)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return repos, now


def cmd_sync(args: argparse.Namespace) -> int:
    root, config_path, readme_path, cache_path = _paths(args)
    config = load_config(config_path)
    repos, fetched_at = _load_repos(args, root, cache_path)
    result = classify(repos, config)
    nav_block = render_nav(config, result, fetched_at=fetched_at)

    if args.dry_run:
        print(nav_block)
        return 0

    changed = update_readme(readme_path, nav_block)
    print(f"{'updated' if changed else 'unchanged'}: {readme_path}")
    print(
        f"total={len(repos)} excluded={len(result.skipped)} "
        f"uncategorized={len(result.groups.get(UNCATEGORIZED, []))}"
    )

    if args.push:
        committed = commit_and_push(
            root,
            [str(readme_path.relative_to(root))],
            "chore: sync starred repositories",
        )
        print("pushed" if committed else "nothing to push")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    root, _, _, cache_path = _paths(args)
    repos, _ = _load_repos(args, root, cache_path)

    topics: Counter[str] = Counter()
    languages: Counter[str] = Counter()
    for repo in repos:
        topics.update(repo.topics)
        if repo.language:
            languages.update([repo.language])

    print(f"total starred repos: {len(repos)}\n")
    print("top languages:")
    for lang, count in languages.most_common(20):
        print(f"  {count:4d}  {lang}")
    print("\ntop topics:")
    for topic, count in topics.most_common(40):
        print(f"  {count:4d}  {topic}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="oh-my-awesome", description=__doc__)
    sub = parser.add_subparsers(dest="command")

    def common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--root", default=".", help="project root (default: cwd)")
        p.add_argument("--config", help="config path (default: <root>/config.yaml)")
        p.add_argument("--readme", help="readme path (default: <root>/README.md)")
        p.add_argument("--offline", action="store_true", help="use cached data, no network")

    sync = sub.add_parser("sync", help="fetch stars and regenerate README")
    common(sync)
    sync.add_argument("--dry-run", action="store_true", help="print markdown instead of writing")
    sync.add_argument("--push", action="store_true", help="commit and push README after render")
    sync.set_defaults(func=cmd_sync)

    stats = sub.add_parser("stats", help="show topic/language statistics for config authoring")
    common(stats)
    stats.set_defaults(func=cmd_stats)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 2
    try:
        return args.func(args)
    except (ConfigError, FetchError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
