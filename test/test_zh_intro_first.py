#!/usr/bin/env python3
"""Lock SKILL.md reading order: frontmatter → 中文导读 → one English H1."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
H1 = re.compile(r"^# [^#\n].*$", re.M)


class ZhIntroFirstTests(unittest.TestCase):
    def test_every_skill_leads_with_chinese_intro(self):
        skills = sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
        self.assertEqual(len(skills), 12)
        for skill_dir in skills:
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), skill_dir.name)
            close = text.find("\n---\n", 4)
            self.assertGreater(close, 0, skill_dir.name)
            after = text[close + 5 :].lstrip()
            self.assertTrue(
                after.startswith("## 中文执行导读\n"),
                f"{skill_dir.name} does not lead with 中文执行导读",
            )
            headings = H1.findall(after)
            self.assertEqual(
                len(headings),
                1,
                f"{skill_dir.name} must have exactly one English H1, got {headings!r}",
            )
            intro, body = after.split("## 中文执行导读", 1)
            self.assertEqual(intro, "")
            self.assertTrue(H1.search(body))
            self.assertNotIn("## 中文执行导读", body)

    def test_readme_map_is_untouched(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Reference", readme)
        self.assertIn("skills/animate/SKILL.md", readme)


if __name__ == "__main__":
    unittest.main()
