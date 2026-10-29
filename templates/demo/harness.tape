# Starter only: replace every {{TOKEN}} before running from the repo root.
# Prepare an isolated project and harness permissions as described in README.md.
Source examples/terminal-demo/style.tape
Output assets/terminal-demo.gif
Hide
Type "export PS1='$ '; set -o pipefail; clear"
Enter
Sleep 500ms
Show
Type "git clone {{REPO_URL}} .claude/skills/{{SKILL_NAME}}"
Sleep 500ms
Hide
Enter
Wait+Screen@30s /done./
Show
Sleep 3s
Type "clear"
Enter
Type 'claude -p "/{{SKILL_NAME}} {{PREVIEW_REQUEST}}"'
Sleep 1s
Hide
Enter
Wait+Screen@180s /{{APPROVAL_PROMPT_REGEX}}/
Show
Sleep 8s
