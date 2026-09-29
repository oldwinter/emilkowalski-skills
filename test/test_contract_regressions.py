#!/usr/bin/env python3
"""Lock distribution, Agent Skills, Swift, and Sonner contracts."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}


def frontmatter(text: str) -> str:
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0] != "":
        raise AssertionError("missing YAML frontmatter")
    return parts[1]


def top_level_keys(block: str) -> set[str]:
    keys: set[str] = set()
    for line in block.splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        keys.add(line.split(":", 1)[0].strip())
    return keys


class ContractRegressionTests(unittest.TestCase):
    def test_install_commands_target_the_fork(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        command = "npx skills@latest add oldwinter/emilkowalski-skills --full-depth"
        self.assertIn(command, readme)
        self.assertNotIn("npx skills@latest add emilkowalski/skills", readme)

    def test_all_skill_frontmatter_uses_spec_fields(self) -> None:
        for entry in sorted(SKILLS.glob("*/SKILL.md")):
            metadata = frontmatter(entry.read_text(encoding="utf-8"))
            unexpected = top_level_keys(metadata) - ALLOWED_FRONTMATTER
            self.assertEqual(unexpected, set(), entry)
            self.assertIn(f"name: {entry.parent.name}", metadata, entry)
            self.assertRegex(metadata, r"(?m)^description: .+")

        for name in ("pick-ui-library", "prototype", "review-animations"):
            metadata = frontmatter((SKILLS / name / "SKILL.md").read_text(encoding="utf-8"))
            self.assertIn('  disable-model-invocation: "true"', metadata, name)

    def test_skill_entries_stay_progressively_loadable(self) -> None:
        for entry in sorted(SKILLS.glob("*/SKILL.md")):
            line_count = len(entry.read_text(encoding="utf-8").splitlines())
            self.assertLessEqual(line_count, 500, f"{entry}: {line_count} lines")

    def test_every_companion_is_referenced_by_its_skill(self) -> None:
        for entry in sorted(SKILLS.glob("*/SKILL.md")):
            body = entry.read_text(encoding="utf-8")
            companions = sorted(
                path.name
                for path in entry.parent.glob("*.md")
                if path.name != "SKILL.md"
            )
            for companion in companions:
                self.assertIn(f"]({companion})", body, f"{entry}: {companion}")
        self.assertFalse((ROOT / "performance-cheatsheet.md").exists())

    def test_swift_release_guidance_is_current(self) -> None:
        swift = (SKILLS / "write-swift" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Toolchain baseline: Swift 6.4", swift)
        self.assertIn("Swift 6.3, when you've measured the need: `@specialized", swift)
        self.assertIn("Shipped in Swift 6.4: `@inline(always)`", swift)
        self.assertNotRegex(swift, r"(?i)6\.4.{0,30}unreleased|unreleased.{0,30}6\.4")
        self.assertNotIn("6.4 ⚠", swift)

    def test_sonner_api_names_defaults_and_routing(self) -> None:
        skill = (SKILLS / "ask-sonner" / "SKILL.md").read_text(encoding="utf-8")
        api = (SKILLS / "ask-sonner" / "API.md").read_text(encoding="utf-8")
        combined = skill + "\n" + api
        self.assertNotIn("getActiveToasts", combined)
        self.assertIn("toast.getToasts()", combined)
        self.assertIn("toast.getHistory()", combined)
        self.assertIn("default 24px", skill)
        self.assertIn("`'24px'`", api)
        self.assertIn("`string[]`", api)
        self.assertIn(r"`number \| string`", api)
        self.assertIn("renders only in an unnamed Toaster", skill)
        self.assertNotIn("every toaster renders the toast", skill)


if __name__ == "__main__":
    unittest.main()
