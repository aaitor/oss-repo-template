"""Check local documentation targets, SVG validity, and template personalization."""
import html
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.venv', 'node_modules', '__pycache__'}


def check_files(root):
    errors = []
    for path in root.rglob('*'):
        if any(part in EXCLUDED for part in path.relative_to(root).parts) or not path.is_file():
            continue
        if path.suffix == '.svg':
            try:
                ET.parse(path)
            except ET.ParseError as exc:
                errors.append(f'{path.relative_to(root)}: invalid SVG: {exc}')
        if path.suffix != '.md':
            continue
        text = re.sub(r'^(`{3,}|~{3,}).*?^\1[^\n]*$', '', path.read_text(), flags=re.M | re.S)
        links = re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
        links += re.findall(r'(?:href|src)=["\x27]([^"\x27]+)', text)
        for link in links:
            parsed = urlsplit(html.unescape(link))
            if parsed.scheme or parsed.netloc or not parsed.path or '{{' in link:
                continue
            base = root if path == root / 'templates/README.md' else path.parent
            target = (root if parsed.path.startswith('/') else base) / unquote(parsed.path).lstrip('/')
            if not target.exists():
                errors.append(f'{path.relative_to(root)}: missing target {link}')
    return errors


def check_setup():
    with tempfile.TemporaryDirectory(prefix='oss-template-check-') as tmp:
        root = Path(tmp)/'repo'
        shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns(*EXCLUDED))
        (root/'.template-state.json').unlink(missing_ok=True)
        command = [sys.executable,str(root/'scripts/customize.py'),'--repo','example-tool','--owner','example-owner',
                   '--title','Example & Tool','--tagline','A useful <result>.','--author','Example Author','--contact','maintainer@example.com']
        result = subprocess.run(command,capture_output=True,text=True)
        if result.returncode:
            return ['Setup failed: '+result.stderr]
        errors = []
        readme = (root/'README.md').read_text()
        if '{{' in readme or 'github.com/example-owner/example-tool' not in readme or 'Example &amp; Tool' not in readme:
            errors.append('Setup metadata replacement/escaping failed.')
        original = (ROOT/'LICENSE').read_text().split('Permission is hereby granted')[1]
        if original not in (root/'LICENSE').read_text():
            errors.append('Setup changed the MIT permission terms.')
        if (root/'assets/social-preview.png').exists():
            errors.append('Setup retained stale social-preview PNG.')
        before = (root/'README.md').read_bytes()
        second = subprocess.run(command,capture_output=True,text=True)
        if second.returncode == 0 or before != (root/'README.md').read_bytes():
            errors.append('Overwrite protection failed.')
        return errors + check_files(root)


def main():
    errors = check_files(ROOT)+check_setup()
    demo = subprocess.run([sys.executable, str(ROOT / 'examples/terminal-demo/demo.py')],
                          capture_output=True, text=True)
    if demo.returncode or 'Temporary example removed on exit.' not in demo.stdout:
        errors.append('Terminal demo failed: ' + demo.stderr)
    if errors:
        print('\n'.join(errors),file=sys.stderr)
        raise SystemExit(1)
    print('OK: local documentation targets, SVGs, customization, escaping, MIT terms, overwrite protection, terminal demo.')


if __name__ == '__main__':
    main()
