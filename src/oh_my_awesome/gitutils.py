from __future__ import annotations

import subprocess
from pathlib import Path


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def commit_and_push(root: Path, paths: list[str], message: str) -> bool:
    """Stage `paths`, commit if there are changes, push. Returns True if a commit happened."""
    add = _git(root, "add", "--", *paths)
    if add.returncode != 0:
        raise RuntimeError(f"git add failed: {add.stderr.strip()}")

    if _git(root, "diff", "--cached", "--quiet").returncode == 0:
        return False

    commit = _git(root, "commit", "-m", message)
    if commit.returncode != 0:
        raise RuntimeError(f"git commit failed: {commit.stderr.strip()}")

    push = _git(root, "push")
    if push.returncode != 0:
        raise RuntimeError(f"git push failed: {push.stderr.strip() or push.stdout.strip()}")
    return True
