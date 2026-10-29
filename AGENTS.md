# Repository demo defaults

When creating or updating a README demo, read `docs/terminal-demo.md` and `templates/demo/README.md`. Use the approved preset in `templates/demo/spec.json` and `examples/terminal-demo/style.tape` unless the user requests a different format.

Default to a short install → actual tool/harness invocation → useful result or approval prompt recording, with a pure black background. For agent skills, show real Claude Code usage rather than a raw CLI payload or fabricated agent conversation. Omit waiting time while preserving real commands and responses. Stop at preview/approval unless the exact external action and content are explicitly authorized. Keep live recordings out of CI.

The working reference and its revision are recorded in the preset. Tailor the demo to the repository; preserve the user's current instructions and the project's working behavior.
