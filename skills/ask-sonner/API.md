# Sonner API Reference

Exact props, types, and defaults. Where a field is accepted by both surfaces, options passed to `toast()` override the same default set through the Toaster's `toastOptions`.

## `<Toaster />`

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `theme` | `string` | `'light'` | `'light'`, `'dark'`, or `'system'`. |
| `richColors` | `boolean` | `false` | Makes error and success states more colorful. |
| `expand` | `boolean` | `false` | Toasts expanded by default (otherwise they expand on hover). |
| `visibleToasts` | `number` | `3` | Amount of visible toasts. |
| `id` | `string` | – | Toaster id, targeted by `toast()`'s `toasterId` option. |
| `position` | `string` | `'bottom-right'` | `top-left`, `top-center`, `top-right`, `bottom-left`, `bottom-center`, `bottom-right`. |
| `closeButton` | `boolean` | `false` | Adds a close button to all toasts. |
| `duration` | `number` | `4000` | Default lifetime in milliseconds. |
| `offset` | `string \| number \| object` | `'24px'` | Offset from screen edges. Object form is per-side: `{ bottom: '24px', right: '16px' }`. |
| `mobileOffset` | `string \| number \| object` | `'16px'` | Offset when screen width < 600px. |
| `swipeDirections` | `SwipeDirection[]` | based on position | Allowed swipe-to-dismiss directions: `top`, `right`, `bottom`, `left`. |
| `dir` | `'rtl' \| 'ltr' \| 'auto'` | document direction | Text directionality. |
| `hotkey` | `string[]` | `['altKey', 'KeyT']` | Keyboard event fields/codes that focus the toaster area. |
| `invert` | `boolean` | `false` | Dark toasts in light mode and vice versa. |
| `toastOptions` | `object` | – | Supported defaults applied to every toast; also carries the Toaster-only `closeButtonAriaLabel`. |
| `gap` | `number` | `14` | Gap between toasts when expanded. |
| `icons` | `object` | – | Replace default icons: `{ success, info, warning, error, loading, close }`; `null` removes one. |
| `className` | `string` | – | Class on the toaster list. |
| `style` | `React.CSSProperties` | – | Inline styles on the toaster list. |
| `customAriaLabel` | `string` | – | Complete accessible label for the toaster region. |
| `containerAriaLabel` | `string` | `'Notifications'` | Base accessible label combined with the hotkey label. |

## `toast()` options

`toast(message, options)` — message is a string, JSX, or a function returning JSX. Returns the toast's id.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `description` | `ReactNode` | – | Renders underneath the title; also accepts a function returning JSX. |
| `closeButton` | `boolean` | `false` | Adds a close button. |
| `invert` | `boolean` | `false` | Dark toast in light mode and vice versa. |
| `duration` | `number` | `4000` | Milliseconds before auto-close. `Infinity` persists the toast. |
| `position` | `string` | `'bottom-right'` | Position of this toast. |
| `dismissible` | `boolean` | `true` | If `false`, the user cannot dismiss the toast. |
| `icon` | `ReactNode` | – | Icon in front of the text; `null` removes the default. |
| `action` | `ReactNode \| { label, onClick }` | – | Primary button; clicking closes the toast unless `onClick` calls `event.preventDefault()`. |
| `cancel` | `ReactNode \| { label, onClick }` | – | Secondary button; clicking closes the toast. |
| `actionButtonStyle` | `object` | `{}` | Styles for the action button. |
| `cancelButtonStyle` | `object` | `{}` | Styles for the cancel button. |
| `id` | `number \| string` | – | Custom id; calling `toast()` again with the same id updates the existing toast. |
| `testId` | `string` | – | Rendered as `data-testid` for e2e tests. |
| `toasterId` | `string` | – | Id of the toaster to render this toast in. |
| `style` | `object` | – | Inline styles for the toast. |
| `className` | `string` | – | Class on the toast root. |
| `descriptionClassName` | `string` | – | Class on the description. |
| `richColors` | `boolean` | – | Overrides the Toaster's rich-color setting for this toast. |
| `classNames` | `object` | – | Classes for `{ toast, title, description, loader, closeButton, cancelButton, actionButton, success, error, info, warning, loading, default, content, icon }`. Needs `!important` unless `unstyled`. |
| `unstyled` | `boolean` | `false` | Removes all default styles. |
| `onDismiss` | `(toast) => void` | – | Fires for close-button, swipe, or programmatic dismissal. |
| `onAutoClose` | `(toast) => void` | – | Fires when the toast closes automatically after `duration`. |

### Toaster `toastOptions`-only setting

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `closeButtonAriaLabel` | `string` | `'Close toast'` | Accessible label for close buttons created by that Toaster. This is not a `toast()` option. |

## Functions

| Function | Purpose |
| --- | --- |
| `toast(message, opts?)` | Render a toast; returns its id. |
| `toast.success / .error / .info / .warning(message, opts?)` | Typed toast with matching icon. |
| `toast.loading(message, opts?)` | Toast with a spinner; update it by id. |
| `toast.promise(promise, { loading, success, error })` | Loading toast that resolves with the promise; `success`/`error` accept strings, JSX, functions of the result, or objects of toast options. |
| `toast.custom((t) => jsx, opts?)` | Headless toast — your JSX, Sonner's behavior. |
| `toast.dismiss(id?)` | Dismiss one toast, or all when called without an id. |
| `toast.getToasts()` | All active toasts, usable outside React. |
| `toast.getHistory()` | Toast history, including dismissed entries retained by Sonner. |
| `useSonner()` | React hook returning `{ toasts }`. |
