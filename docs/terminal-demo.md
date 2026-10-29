# From working command to animated terminal demo

The README animation records a real local workflow: create a fresh project identity, generate its README and banners, and inspect the output. The [Python example](../examples/terminal-demo/demo.py) runs customization in a disposable copy, so you can replay it safely.

## 1. Try the workflow

From the repository root:

```bash
python3 examples/terminal-demo/demo.py
```

You should see the customization output, then these generated files:

```text
README.md
assets/hero.svg
assets/social-preview.svg

Done. Temporary example removed on exit.
```

No account, API key, or paid service is needed. This command demonstrates the publishing template; replace it with your actual tool's workflow in generated projects.

## 2. Install the recorder

Use [Charmbracelet VHS's official installation instructions](https://github.com/charmbracelet/vhs#installation). VHS needs `ttyd` and `ffmpeg` on PATH; Python 3.10+ runs this example. This recording was produced with VHS 0.12.1 and ttyd 1.7.7. The example uses Bash and DejaVu Sans Mono; install that font or change `FontFamily` in the theme.

## 3. Render the GIF

Run from the repository root, with `vhs`, `ttyd`, `ffmpeg`, and `python3` available:

```bash
vhs examples/terminal-demo/demo.tape
```

The tape imports [the shared theme](../examples/terminal-demo/theme.tape), types the command, waits for actual completion, and holds the final result for five seconds. Its output is `assets/terminal-demo.gif`. Keep this generated GIF in Git so GitHub renders it directly without requiring a player.

## 4. Put it beside the instructions

Embed the result in the README, followed by a text description and the same runnable command:

```markdown
![Terminal demo: generate project documentation and banners](assets/terminal-demo.gif)
```

Readers who cannot view the animation can follow the text tutorial and expected output. Keep recordings focused on one useful result, around 10–20 seconds long, with legible text and a quiet terminal theme.

## 5. Adapt it for your next tool

1. Replace `examples/terminal-demo/demo.py` with a small, repeatable real workflow using synthetic input.
2. Update the command and completion expression in `demo.tape`.
3. Keep shell preparation hidden, while showing the actual command and its real output.
4. Render and watch the result. Confirm it matches the written quick start and contains no secrets or personal paths.
5. Replace the inherited template GIF before publishing a generated project.

The normal CI runs the Python example as a smoke check. Recording remains a local, explicit action so documentation checks do not need a browser, encoder, or network access. The theme originates in [aaitor/assets](https://github.com/aaitor/assets); its pinned source is recorded in `shared-assets.json`.
