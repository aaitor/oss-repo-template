# A terminal demo you can reproduce

This example records real template customization in a temporary copy. It needs Python 3.10+ and Node.js 18+ to run; it makes no API calls, changes no GitHub settings, and deletes the temporary project on exit.

```bash
python3 examples/terminal-demo/demo.py
```

Expected result: a generated README, hero SVG, and social-preview SVG, followed by `Done. Temporary example removed on exit.` See the [practical tutorial](../../docs/terminal-demo.md) for the recording steps and instructions for adapting it to your tool.

## Default for future demos

Use the [approved preset](../../templates/demo/README.md): 1280 × 640, pure black background, 20px DejaVu Sans Mono, and a short install → real invocation → result sequence. The [style file](style.tape) applies the defaults. For agent skills, replace this local CLI example with actual Claude Code usage and stop at the approval prompt unless publishing is explicitly authorized.
