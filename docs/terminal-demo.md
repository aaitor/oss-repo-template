# Record a short, real repository demo

Use the final [approved demo preset](../templates/demo/README.md) for new recordings. It comes from the user-approved LinkedIn skill demo: actual installation and Claude Code usage, a pure black background, and a stop at publishing approval. Exact values and the pinned reference revision are stored in [spec.json](../templates/demo/spec.json).

## Default specification

| Setting | Default |
| --- | --- |
| Sequence | Install → actual tool/harness invocation → useful result or approval prompt |
| Agent skill harness | Real Claude Code session, with the installed repository skill |
| Canvas | 1280 × 640 |
| Background | Pure black `#000000` |
| Text / accent | `#F4F7FB` / `#89E5CC` |
| Font | DejaVu Sans Mono, 20px |
| Padding / corners | 28px / square (0px radius) |
| Window bar | Colorful |
| Typing | 25ms per character |
| Length | Aim for 10–20 seconds; approved reference is about 17 seconds |
| Holds | 3s after installation, 1s before harness output, 8s on final response |
| Waiting | Use `Hide` → execute/wait → `Show` to omit cloning/model latency |
| Timeouts | 30s for clone completion; 180s for the harness |
| Output | `assets/terminal-demo.gif` |

Import [style.tape](../examples/terminal-demo/style.tape) to apply the visual defaults. For an agent skill, adapt [harness.tape](../templates/demo/harness.tape) and the [working recorder reference](../templates/demo/README.md#working-recorder-reference). Show the skill being installed and used through the actual harness. Keep raw JSON, debug logs, setup details, and long authorization instructions out of the main recording.

Record real commands and actual output. A credential-free fixture can be a separate exercise, but must not replace the real harness demo. Use an isolated temporary project and narrowly scoped session permissions, without changing global settings or bypassing permissions. Stop at the preview/approval question by default. Any actual publishing still needs explicit approval of the exact content.

Watch the exported GIF before committing: confirm black background, readable text, correct output, no credentials or personal identifiers, and no claims of actions that did not happen. Document prerequisites, what was recorded, where pauses were omitted, and the command to regenerate it. Run live recordings manually; CI should use offline checks only.

## This template's runnable example

The template itself demonstrates its local customization CLI. It uses the approved style and a real temporary checkout, and does not launch an AI harness or call an external service. Generated agent-skill projects should replace this example with the harness workflow above.

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

Use [Charmbracelet VHS's official installation instructions](https://github.com/charmbracelet/vhs#installation). VHS needs `ttyd` and `ffmpeg` on PATH; Python 3.10+ and Node.js 18+ run this example. This recording was produced with VHS 0.12.1 and ttyd 1.7.7. The example uses Bash and DejaVu Sans Mono; install that font or change `FontFamily` in the theme.

## 3. Render the GIF

Run from the repository root, with `vhs`, `ttyd`, `ffmpeg`, and `python3` available:

```bash
vhs examples/terminal-demo/demo.tape
```

The tape imports [the approved style](../examples/terminal-demo/style.tape), types the command, waits for actual completion, and holds the final result for eight seconds. Its output is `assets/terminal-demo.gif`. Keep this generated GIF in Git so GitHub renders it directly without requiring a player.

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
