# Emil Kowalski Skills 中文化档案

同步上游后先读本档案，再处理新增或变更内容。

## 项目定位

- 上游项目：`emilkowalski/skills`
- 中文 fork：`oldwinter/emilkowalski-skills`
- 当前同步上游 commit：`78761e1b57f9a932847d3d66894e3cc94ff2af3b`
- 主要安装面：skills CLI、直接读取 `skills/`
- 中文 runtime 入口：10 个 `skills/*/SKILL.md`

## 中文化目标

保留 Emil 的动画与界面设计原则、示例术语、代码和精确数值；每个 skill 入口增加中文执行导读，帮助中文用户选择、调用和验证对应工作流。产品名、库名、动画术语、URL、命令和 skill slug 不翻译。

## 安装与交付

```bash
npx skills add oldwinter/emilkowalski-skills --full-depth
```

安装后 runtime 直接读取中文 fork 的 `skills/*/SKILL.md`；README 中的上游链接仅保留作者归属和参考资料。

## 同步后检查

- `git diff --check`
- `rg -n '^(<<<<<<<|=======|>>>>>>>)$' .`
- 10 个 `skills/*/SKILL.md` 均包含中文导读并保留原 frontmatter `name`
