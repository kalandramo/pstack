#!/usr/bin/env python3
"""Manage pstack WorkBuddy skills: install, validate, status.

Read-only commands (validate, status) never copy. install is idempotent
(overwrite-merge, no deletion) and never touches TARGET dirs not in SOURCE.
"""
import argparse
import json
import shutil
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import re

SOURCE = Path("/Users/moweilong/Workspace/go/src/github.com/kalandramo/pstack/workbuddy")
TARGET = Path.home() / ".workbuddy" / "skills"
FORK_MARKER = "local-fork:kalandramo/pstack"
REQUIRED_KEYS = {"name", "version", "display_name", "description", "description_zh", "description_en"}


class Status(Enum):
    OK = "OK"
    MISSING_FRONTMATTER = "MISSING_FRONTMATTER"
    MISSING_KEYS = "MISSING_KEYS"
    MISSING_META = "MISSING_META"
    INVALID_META = "INVALID_META"


@dataclass
class SkillRecord:
    name: str
    src_dir: Path | None = None
    tgt_dir: Path | None = None
    frontmatter: dict = field(default_factory=dict)
    meta: dict | None = None
    meta_error: str | None = None
    status: Status = Status.OK
    errors: list[str] = field(default_factory=list)


def parse_frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (FileNotFoundError, UnicodeDecodeError):
        return None
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm


def get_meta_source(d: Path) -> str | None:
    try:
        data = json.loads((d / "_skillhub_meta.json").read_text(encoding="utf-8"))
        return data.get("source")
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError):
        return None


def validate_skill(rec: SkillRecord) -> SkillRecord:
    fm = parse_frontmatter(rec.tgt_dir / "SKILL.md") if rec.tgt_dir else None
    rec.frontmatter = fm or {}
    if fm is None:
        rec.status = Status.MISSING_FRONTMATTER
        rec.errors.append("no frontmatter in SKILL.md")
        return rec
    missing = REQUIRED_KEYS - set(rec.frontmatter)
    if missing:
        rec.status = Status.MISSING_KEYS
        rec.errors.append("missing keys: " + ", ".join(sorted(missing)))
        return rec
    try:
        text = (rec.tgt_dir / "_skillhub_meta.json").read_text(encoding="utf-8")
    except FileNotFoundError:
        rec.status = Status.MISSING_META
        rec.errors.append("missing _skillhub_meta.json")
        return rec
    except UnicodeDecodeError:
        rec.status = Status.INVALID_META
        rec.meta_error = "unicode decode error"
        rec.errors.append(rec.meta_error)
        return rec
    try:
        rec.meta = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        rec.status = Status.INVALID_META
        rec.meta_error = "json parse error"
        rec.errors.append(rec.meta_error)
        return rec
    rec.status = Status.OK
    return rec


def gather():
    source_names = {e.name for e in SOURCE.iterdir() if e.is_dir()} if SOURCE.exists() else set()
    targets = [e for e in TARGET.iterdir() if e.is_dir()] if TARGET.exists() else []
    in_scope, foreign = [], []
    for d in targets:
        ms = get_meta_source(d)
        if ms is not None and ms != FORK_MARKER:
            foreign.append(d.name)
            continue
        if d.name in source_names or ms == FORK_MARKER:
            in_scope.append(d)
    orphans = [d for d in in_scope if d.name not in source_names]
    table = [d for d in in_scope if d.name in source_names]
    not_installed = [n for n in source_names if not (TARGET / n).is_dir()]
    return source_names, table, orphans, not_installed, foreign


def print_report(table, orphans, not_installed, foreign):
    print(f"\n{'skill':<32} status")
    print("-" * 40)
    for d in table:
        rec = validate_skill(SkillRecord(name=d.name, tgt_dir=d))
        print(f"{rec.name:<32} {rec.status.value}")
    if orphans:
        print("\norphans (target fork dirs absent from source):")
        for d in orphans:
            rec = validate_skill(SkillRecord(name=d.name, tgt_dir=d))
            print(f"  {rec.name:<30} {rec.status.value}")
    if not_installed:
        print("\nnot-installed (source skills absent from target):")
        for n in not_installed:
            print(f"  {n}")
    if foreign:
        print("\nforeign (not pstack forks, skipped):")
        for n in foreign:
            print(f"  {n}")
    return all(
        validate_skill(SkillRecord(name=d.name, tgt_dir=d)).status == Status.OK
        for d in table + orphans
    )


def cmd_install(args):
    failures = []
    if SOURCE.exists():
        for e in sorted(SOURCE.iterdir()):
            if not e.is_dir():
                continue
            tgt = TARGET / e.name
            try:
                shutil.copytree(e, tgt, dirs_exist_ok=True)
            except OSError as ex:
                failures.append(f"{e.name}: {ex}")
    if failures:
        print("copy failures:")
        for f in failures:
            print(f"  {f}")
    _, table, orphans, not_installed, foreign = gather()
    all_ok = print_report(table, orphans, not_installed, foreign)
    ok = (not not_installed) and all_ok and (not failures)
    sys.exit(0 if ok else 1)


def cmd_validate(args):
    _, table, orphans, not_installed, foreign = gather()
    all_ok = print_report(table, orphans, not_installed, foreign)
    sys.exit(0 if all_ok else 1)


def cmd_status(args):
    _, table, orphans, not_installed, foreign = gather()
    print_report(table, orphans, not_installed, foreign)
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(description="Manage pstack WorkBuddy skills")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("install")
    sub.add_parser("validate")
    sub.add_parser("status")
    args = p.parse_args()
    {"install": cmd_install, "validate": cmd_validate, "status": cmd_status}[args.cmd](args)


if __name__ == "__main__":
    main()
