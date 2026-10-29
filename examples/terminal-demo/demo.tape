# Run from the repository root: vhs examples/terminal-demo/demo.tape
# This template's own demo is a CLI example; agent skills use templates/demo/harness.tape.
Source examples/terminal-demo/style.tape
Output assets/terminal-demo.gif
Hide
Type "export PS1='$ '; clear"
Enter
Sleep 500ms
Show
Type "python3 examples/terminal-demo/demo.py"
Sleep 1s
Hide
Enter
Wait+Screen@30s /Temporary example removed/
Show
Sleep 8s
