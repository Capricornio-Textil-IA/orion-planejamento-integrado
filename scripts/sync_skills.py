"""Gera cópias de skills para Claude Code sem depender de links simbólicos."""

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / ".claude" / "skills"


def snapshot(folder: Path) -> dict[str, bytes]:
    return {
        str(file.relative_to(folder)): file.read_bytes()
        for file in folder.rglob("*")
        if file.is_file()
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    folders = sorted(path for path in SOURCE.iterdir() if (path / "SKILL.md").is_file())
    expected = {
        f"{folder.name}/{name}": content
        for folder in folders
        for name, content in snapshot(folder).items()
    }
    if not expected:
        raise SystemExit("Nenhuma skill canônica encontrada; sincronização interrompida.")
    if args.check:
        if snapshot(TARGET) != expected:
            print("Skills divergentes: execute python3 scripts/sync_skills.py")
            return 1
        print(f"{len(folders)} skills sincronizadas.")
        return 0
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)
    for folder in folders:
        shutil.copytree(folder, TARGET / folder.name)
    print(f"{len(folders)} skills geradas em .claude/skills/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
