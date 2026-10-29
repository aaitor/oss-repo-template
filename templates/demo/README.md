# Approved repository demo preset

This is the final format approved for [Publish to LinkedIn](https://github.com/aaitor/skill-publish-to-linkedin/blob/fe46d8ae5e222d77fbda9c1169a12b2907130910/assets/terminal-demo.gif). Use it by default for future repository demos. The reference is a real Claude Code recording, about 17 seconds long, stopping at publishing approval.

- [spec.json](spec.json): machine-readable dimensions, colors, typography, timing, sequence, and reference revision.
- [style.tape](../../examples/terminal-demo/style.tape): reusable VHS configuration; imports the shared theme and overrides it with the approved black style.
- [harness.tape](harness.tape): starter showing skill installation, real Claude Code invocation, and the approval prompt.
- [Recording guide](../../docs/terminal-demo.md): workflow and verification.

## Adapt the harness starter

1. Copy `harness.tape` into `examples/terminal-demo/` and replace its tokens with the actual repository URL, skill name, preview request, and completion expression.
2. Prepare an isolated temporary project with the example input and the skill's real prerequisites. Install the skill visibly using the clone command. Do not overwrite an existing installed skill.
3. Configure the harness for that isolated project. Allow only the tools needed for the demonstrated status/preview workflow; keep global settings unchanged and do not bypass permissions.
4. Run the actual harness. Keep setup and clone/model waiting time hidden using `Hide`/`Show`; preserve the real command and final response.
5. Stop at the approval prompt by default. Confirm the exact content and explicit authorization before any actual external write.
6. Inspect the finished GIF, then replace `assets/terminal-demo.gif` and update the project's reproduction guide.

A starter is not an executable demo until its tokens and project setup are filled in. For a CLI or library, replace Claude with the real entrypoint while keeping the same visual style and short sequence.

## Working recorder reference

The [approved Python recorder](https://github.com/aaitor/skill-publish-to-linkedin/blob/fe46d8ae5e222d77fbda9c1169a12b2907130910/examples/record_demo.py) shows a complete isolated-project setup, real installation, real Claude Code invocation, and output copied back only after recording finishes. Its [recording instructions](https://github.com/aaitor/skill-publish-to-linkedin/blob/fe46d8ae5e222d77fbda9c1169a12b2907130910/examples/README.md) describe prerequisites and session-specific tool configuration. Adapt its project-specific permissions, input, and prompt; do not transplant LinkedIn-specific behavior into unrelated projects.

Do not replay invented success messages or a fake agent transcript. Keep credential-free mock examples separate from the main harness recording. Live recording stays manual and is never executed by CI.
