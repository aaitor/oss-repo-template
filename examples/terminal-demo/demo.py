"""Demonstrate customization in a disposable checkout; never edit the real repo."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]

with tempfile.TemporaryDirectory(prefix='oss-demo-') as temporary:
    project = Path(temporary) / 'my-tool'
    shutil.copytree(ROOT, project, ignore=shutil.ignore_patterns(
        '.git', '.venv', '__pycache__', 'node_modules', '.template-state.json'))
    print('Create a project from the template', flush=True)
    print('$ python3 scripts/customize.py --repo my-tool --title "My Tool" ' + chr(92), flush=True)
    print('    --tagline "Make everyday work a little easier."', flush=True)
    subprocess.run([
        sys.executable, str(project / 'scripts/customize.py'),
        '--repo', 'my-tool', '--title', 'My Tool',
        '--tagline', 'Make everyday work a little easier.',
    ], check=True)
    print('\nGenerated files:', flush=True)
    for name in ['README.md', 'assets/hero.svg', 'assets/social-preview.svg']:
        path = project / name
        if not path.is_file():
            raise RuntimeError(f'Missing generated file: {name}')
        print(f'  {name}', flush=True)
    print('\nDone. Temporary example removed on exit.', flush=True)
