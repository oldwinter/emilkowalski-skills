#!/usr/bin/env python3
"""Lock README Reference to a job → skill map plus companion files."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILLS = ROOT / "skills"

SKILL_NAMES = (
    "animate",
    "animate-expo",
    "animation-vocabulary",
    "apple-design",
    "ask-sonner",
    "emil-design-eng",
    "find-animation-opportunities",
    "improve-animations",
    "pick-ui-library",
    "prototype",
    "review-animations",
    "write-swift",
)

COMPANIONS = (
    "skills/animate/RECIPES.md",
    "skills/animate-expo/RECIPES.md",
    "skills/review-animations/STANDARDS.md",
    "skills/improve-animations/AUDIT.md",
    "skills/improve-animations/PLAN-TEMPLATE.md",
    "skills/prototype/PICKER.md",
    "skills/ask-sonner/API.md",
)

EXCLUSIVE_JOBS = (
    ("Write one web animation", "animate", "Review a diff"),
    ("Write one React Native / Expo animation", "animate-expo", "web CSS"),
    ("Review a motion diff", "review-animations", "Write features"),
    ("Audit every animation and write plans", "improve-animations", "Apply the fixes"),
    ("Find places that should (or must not) move", "find-animation-opportunities", "Implement"),
)


def reference_section(text: str) -> str:
    match = re.search(r"^## Reference\n(.*)\Z", text, flags=re.M | re.S)
    if not match:
        raise AssertionError("missing ## Reference")
    return match.group(1)


def table_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r":?-{3,}:?", cells[0]):
            continue
        rows.append(cells)
    return rows


class ReadmeSkillMapTests(unittest.TestCase):
    def test_job_table_separates_exclusive_motion_skills(self) -> None:
        section = reference_section(README.read_text(encoding="utf-8"))
        rows = table_rows(section)
        self.assertGreaterEqual(len(rows), 2, "job table is missing")
        self.assertEqual(rows[0], ["You need to", "Use", "Does not"])
        body = rows[1:]
        self.assertEqual(len(body), len(SKILL_NAMES), body)
        by_job = {row[0]: row for row in body}
        for job, skill, forbidden in EXCLUSIVE_JOBS:
            self.assertIn(job, by_job, job)
            use, does_not = by_job[job][1], by_job[job][2]
            self.assertIn(f"](./skills/{skill}/SKILL.md)", use)
            self.assertIn(forbidden, does_not)

    def test_grouped_catalog_links_skills_and_companions(self) -> None:
        readme = README.read_text(encoding="utf-8")
        section = reference_section(readme)
        self.assertIn("### Motion — write", section)
        self.assertIn("### Motion — review, plan, hunt", section)
        self.assertIn("### Design, libraries, native", section)
        for name in SKILL_NAMES:
            rel = f"skills/{name}/SKILL.md"
            self.assertIn(f"](./{rel})", section, name)
            self.assertTrue((ROOT / rel).is_file(), rel)
        for rel in COMPANIONS:
            self.assertIn(f"](./{rel})", section, rel)
            self.assertTrue((ROOT / rel).is_file(), rel)
        self.assertIn("npx skills@latest add emilkowalski/skills", readme)
        self.assertNotIn("skills/animate/SKILL.md)** — Builds an animation from scratch", readme)


if __name__ == "__main__":
    unittest.main()
