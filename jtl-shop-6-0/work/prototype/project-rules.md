# Project rules (give this file to your AI coding tool)

*Most AI coding tools read a rules file from the project folder every time. Your tool may expect a particular file name (check its documentation); copy this text into that file, or keep this one and tell the tool to read it first.*

## What you are building
A clickable prototype of the flow in `work/options.md`, as plain HTML, CSS and a little JavaScript. It is a reference for developers, not production code.

## Use only the design system
- Use only the variables in `design-system/tokens.css` and the components in `design-system/components.css`. Do not write raw colours, font sizes or spacing values.
- Look at `design-system/components.html` to see what exists. If a component you need is missing, **say so and stop**; do not invent one.
- Do not add libraries, frameworks, fonts or images from other sites.

## Accessibility rules
- One `<h1>` per screen, inside `<main>`. Every input has a visible `<label>`.
- Everything works with a keyboard; focus is visible; move focus to the new heading when the screen changes.
- Errors say what went wrong and how to fix it, are shown next to the field, and are announced (`role="alert"`).
- Meaning is never carried by colour alone. Touch targets are at least 44 px.

## How to work
- Build one screen at a time. After each change, list the files you changed.
- Use real content from `work/options.md` (the content notes), not "lorem ipsum".
- If an instruction is unclear or the information is missing, say "unknown" and ask. Do not guess.
- Do not change files I did not ask you to change.
