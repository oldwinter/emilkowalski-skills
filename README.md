<a href="https://animations.dev/">
<img width="320" height="168" alt="opengraph-image-pwu6ef" src="https://github.com/user-attachments/assets/a405a37f-1a1a-4e8d-8fd6-269ee6d4fba6" />
</a>

# Skills For Designers and Engineers

## 中文版安装（oldwinter fork）

这是上游 `emilkowalski/skills` 的中文化 fork。安装后直接读取 `skills/*/SKILL.md` 中的中文执行导读和上游权威正文；当前 12 个 skill（含 `animate`、`animate-expo`、`write-swift` 与 `ask-sonner`）均含中文执行导读。

```bash
npx skills add oldwinter/emilkowalski-skills --full-depth
```

[![skills.sh](https://skills.sh/b/emilkowalski/skills)](https://skills.sh/emilkowalski/skills)

For designers and engineers to help them build better user interfaces.

Knowing whether you made a right choice when it comes to animations, or design in general, is hard. These skills aim to help you get to those right decisions faster.

They are based on my years of experience working at companies like Vercel and Linear.

All the skills here are a side-effect of domain-expertise. AI doesn’t replace such expertise, it amplifies what you can get out of it and makes you way better relative to others.

So learn to code, design, or develop expertise in any other field. It’s extremely valuable.

You can stay up to date with my skills here:

[Sign Up To The Newsletter](https://animations.dev/skills)

## Install

```bash
npx skills@latest add emilkowalski/skills
```

## Why use it?

Agents don’t have great taste

I have seen plenty of times that agents don’t pick the right ingredients for an animation. An `ease-in` easing for an enter animation when it’s supposed to be `ease-out` ([here’s why](https://emilkowal.ski/ui/7-practical-animation-tips#4.-choose-the-right-easing)). Or they choose a solid border instead of a semi-transparent shadow for your UIs.

All these small things compound and make your interface either amazing, or just... not that great.

As explained in [Agents with Taste](https://emilkowal.ski/ui/agents-with-taste), these skills list all the little mistakes agents can potentially make and explain how to fix them.

This is your shortcut to great interfaces. A shortcut to stand out in a sea of slop.

## Reference

Pick by the job. These skills do not overlap: writing motion, reviewing a diff, auditing a repo, and hunting for places that should move are four different next steps.

| You need to | Use | Does not |
| --- | --- | --- |
| Write one web animation | [animate](./skills/animate/SKILL.md) | Review a diff, audit a repo, or hunt for opportunities |
| Write one React Native / Expo animation | [animate-expo](./skills/animate-expo/SKILL.md) | Touch web CSS / Motion |
| Review a motion diff | [review-animations](./skills/review-animations/SKILL.md) | Write features or change code |
| Audit every animation and write plans | [improve-animations](./skills/improve-animations/SKILL.md) | Apply the fixes |
| Find places that should (or must not) move | [find-animation-opportunities](./skills/find-animation-opportunities/SKILL.md) | Implement or review existing motion |
| Name a motion effect | [animation-vocabulary](./skills/animation-vocabulary/SKILL.md) | Design or build it |
| Ask a design-engineering question | [emil-design-eng](./skills/emil-design-eng/SKILL.md) | Run a specialized motion workflow |
| Build Apple-style fluid UI on the web | [apple-design](./skills/apple-design/SKILL.md) | Write Expo or Swift |
| Pick a library instead of hand-rolling | [pick-ui-library](./skills/pick-ui-library/SKILL.md) | Invent a toast, dropdown, or chart |
| Compare several live UI variants | [prototype](./skills/prototype/SKILL.md) | Review existing UI or pick a dependency |
| Wire or debug [Sonner](https://sonner.emilkowal.ski) | [ask-sonner](./skills/ask-sonner/SKILL.md) | Hand-roll a toast |
| Write or review Swift | [write-swift](./skills/write-swift/SKILL.md) | Touch web or Expo motion |

### Motion — write

- **[animate](./skills/animate/SKILL.md)** — Implements one web animation (curve, duration, properties). Exact recipes: [RECIPES.md](./skills/animate/RECIPES.md).
- **[animate-expo](./skills/animate-expo/SKILL.md)** — Same bar for Expo: gestures, sheets, haptics, screen transitions, UI-thread motion. Recipes: [RECIPES.md](./skills/animate-expo/RECIPES.md).

### Motion — review, plan, hunt

- **[review-animations](./skills/review-animations/SKILL.md)** — Strict review of a motion diff. Precise values: [STANDARDS.md](./skills/review-animations/STANDARDS.md).
- **[improve-animations](./skills/improve-animations/SKILL.md)** — Read-only audit, then self-contained plans. Playbook: [AUDIT.md](./skills/improve-animations/AUDIT.md). Plan shape: [PLAN-TEMPLATE.md](./skills/improve-animations/PLAN-TEMPLATE.md).
- **[find-animation-opportunities](./skills/find-animation-opportunities/SKILL.md)** — Search for seams that should move, and reject the ones that must not.

### Design, libraries, native

- **[emil-design-eng](./skills/emil-design-eng/SKILL.md)** — General design-engineering philosophy (animation plus UI polish).
- **[animation-vocabulary](./skills/animation-vocabulary/SKILL.md)** — Reverse-lookup: vague description → exact motion term.
- **[apple-design](./skills/apple-design/SKILL.md)** — Apple interface and fluid-motion principles, translated for the web.
- **[pick-ui-library](./skills/pick-ui-library/SKILL.md)** — Opinionated library pick for toasts, menus, charts, and similar tasks.
- **[prototype](./skills/prototype/SKILL.md)** — Build several genuinely different versions behind a picker. Picker spec: [PICKER.md](./skills/prototype/PICKER.md).
- **[ask-sonner](./skills/ask-sonner/SKILL.md)** — Sonner setup, styling, recipes, and common failures. Prop tables: [API.md](./skills/ask-sonner/API.md).
- **[write-swift](./skills/write-swift/SKILL.md)** — Modern Swift: value types, Swift 6 concurrency, generics, performance, Swift Testing.
