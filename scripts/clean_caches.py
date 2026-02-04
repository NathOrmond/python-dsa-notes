#!/usr/bin/env python3
"""
Clean Python cache and build artifacts across the repository.

Removes:
- __pycache__ directories
- *.pyc, *.pyo, *.pyd files
- .pytest_cache, .mypy_cache, .ruff_cache, .cache
- build, dist, and *.egg-info directories

Usage:
  python scripts/clean_caches.py            # clean from repo root (auto-detected)
  python scripts/clean_caches.py --dry-run  # show what would be removed
  python scripts/clean_caches.py --root PATH
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Iterable, List


CACHE_DIR_NAMES: List[str] = [
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".cache",
    "build",
    "dist",
]

FILE_SUFFIXES: List[str] = [
    ".pyc",
    ".pyo",
    ".pyd",
]


def find_repo_root(start: Path) -> Path:
    """Ascend from start to locate repo root by presence of .git or pyproject.toml."""
    current = start.resolve()
    for parent in [current, *current.parents]:
        if (parent / ".git").exists() or (parent / "pyproject.toml").exists():
            return parent
    # Fallback to the directory containing scripts/
    return start.resolve()


def remove_dir(path: Path, *, dry_run: bool, verbose: bool) -> bool:
    if not path.exists():
        return False
    if verbose or dry_run:
        print(f"[DIR]  {path}")
    if not dry_run:
        shutil.rmtree(path, ignore_errors=True)
    return True


def remove_file(path: Path, *, dry_run: bool, verbose: bool) -> bool:
    if not path.exists():
        return False
    if verbose or dry_run:
        print(f"[FILE] {path}")
    if not dry_run:
        try:
            path.unlink()
        except FileNotFoundError:
            return False
    return True


def should_remove_dir(dirname: str) -> bool:
    if dirname in CACHE_DIR_NAMES:
        return True
    if dirname.endswith(".egg-info"):
        return True
    return False


def should_remove_file(filename: str) -> bool:
    return any(filename.endswith(suffix) for suffix in FILE_SUFFIXES)


def clean(root: Path, *, dry_run: bool, verbose: bool) -> None:
    removed_dirs = 0
    removed_files = 0

    # First pass: remove matching directories
    for dirpath, dirnames, filenames in os.walk(root):
        # Copy to avoid modifying while iterating
        for d in list(dirnames):
            if should_remove_dir(d):
                target = Path(dirpath) / d
                if remove_dir(target, dry_run=dry_run, verbose=verbose):
                    removed_dirs += 1
                # Prevent descending into a directory that was (or will be) removed
                try:
                    dirnames.remove(d)
                except ValueError:
                    pass

    # Second pass: remove matching files
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            if should_remove_file(f):
                target = Path(dirpath) / f
                if remove_file(target, dry_run=dry_run, verbose=verbose):
                    removed_files += 1

    print(
        f"Done. Removed {removed_dirs} director{'y' if removed_dirs == 1 else 'ies'} "
        f"and {removed_files} file{'s' if removed_files != 1 else ''}."
    )


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean Python cache/build artifacts.")
    parser.add_argument(
        "--root",
        type=Path,
        help="Root directory to clean (default: auto-detect repo root)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be removed, without deleting anything",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each removed path",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)

    script_dir = Path(__file__).resolve().parent
    default_root = find_repo_root(script_dir.parent)
    root = (args.root or default_root).resolve()

    if not root.exists():
        print(f"Root path does not exist: {root}", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"[DRY-RUN] Cleaning under: {root}")
    else:
        print(f"Cleaning under: {root}")

    clean(root, dry_run=args.dry_run, verbose=args.verbose)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))


