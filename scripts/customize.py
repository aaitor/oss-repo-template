"""Personalize a fresh template checkout using the Python standard library."""
import argparse
import datetime
import html
import json
from pathlib import Path
import re

from branding import artwork

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--title', required=True, help='At most 32 characters')
    parser.add_argument('--tagline', required=True, help='At most 76 characters')
    parser.add_argument('--owner', default='aaitor')
    parser.add_argument('--author', default='Aitor Argomaniz')
    parser.add_argument('--contact', default='aaitor@gmail.com', help='Public reporting email')
    parser.add_argument('--force', action='store_true', help='Overwrite customized README/artwork')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,99}', args.repo):
        parser.error('Use a valid GitHub repository name.')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', args.owner):
        parser.error('Use a valid GitHub owner.')
    for name, limit in [('title',32), ('tagline',76), ('author',48)]:
        value = getattr(args,name)
        if not value.strip() or len(value)>limit or any(ord(c)<32 for c in value):
            parser.error(f'{name} must contain 1–{limit} printable characters.')
    if not re.fullmatch(r'[A-Za-z0-9.!#$%&\x27*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',args.contact):
        parser.error('Supply a reporting email address.')
    state = ROOT / '.template-state.json'
    if state.exists() and not args.force:
        parser.error('Already customized. Save your work before --force; README and artwork will be replaced.')
    previous = json.loads(state.read_text()) if state.exists() else dict(owner='aaitor',repo='oss-repo-template',author='Aitor Argomaniz',contact='aaitor@gmail.com')
    starter = (ROOT/'templates/README.md').read_text()
    values = {key.upper():html.escape(getattr(args,key)) for key in ('repo','owner','title','tagline','author')}
    readme = re.sub(r'\{\{(REPO|OWNER|TITLE|TAGLINE|AUTHOR)\}\}',lambda m:values[m[1]],starter)
    for name in ('CONTRIBUTING.md','CODE_OF_CONDUCT.md','SECURITY.md'):
        path = ROOT/name
        text = path.read_text().replace(f"github.com/{previous['owner']}/{previous['repo']}",f'github.com/{args.owner}/{args.repo}')
        text = text.replace(f"github.com/{previous['owner']})",f'github.com/{args.owner})')
        text = text.replace(previous['author'],args.author).replace(previous['contact'],args.contact)
        path.write_text(text)
    (ROOT/'README.md').write_text(readme)
    for filename,height in [('hero.svg',420),('social-preview.svg',640)]:
        (ROOT/'assets'/filename).write_text(artwork(args.title,args.tagline,args.owner,args.author,height)+'\n')
    (ROOT/'assets/social-preview.png').unlink(missing_ok=True)
    notice = f'Copyright (c) {datetime.date.today().year} {args.author}'
    path = ROOT/'LICENSE'
    text = path.read_text()
    if notice not in text:
        path.write_text(text.replace('MIT License\n',f'MIT License\n\n{notice}',1))
    (ROOT/'CHANGELOG.md').write_text('# Changelog\n\n## Unreleased\n\nRecord your project changes here before the first release.\n')
    state.write_text(json.dumps({key:getattr(args,key) for key in ('owner','repo','author','contact')},indent=2)+'\n')
    print(f'Customized {args.owner}/{args.repo}.')
    print('Review README.md; add real installation steps and a demo.')
    print('Export assets/social-preview.svg to PNG.')
    print('Upload it in GitHub Settings → Social preview.')
    print('Run python3 scripts/check.py, then review and commit the changes.')


if __name__ == '__main__':
    main()
