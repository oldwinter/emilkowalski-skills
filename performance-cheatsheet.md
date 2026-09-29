# 性能速查表

| 问题 | 解决方法 |
| --- | --- |
| 动画卡顿 | 动画化 `transform` 或 `opacity`，不要动画化 `width` 或 `top` |
| 长列表滚动缓慢 | 使用虚拟化，只渲染可见内容 |
| 模糊效果造成性能问题 | 动态 `blur()` 保持在 20px 以下 |
| Motion 的 `x` 或 `y` 掉帧 | 改为动画化完整的 `transform` 字符串 |
| 意外属性参与动画 | 不要使用 `transition: all`，明确列出属性 |
| React 每帧重新渲染 | 写入 `ref.current.style`，不要写入 state |
| 动画开始时元素偏移 1px | 仅在实际出现偏移后添加 `will-change: transform` |
