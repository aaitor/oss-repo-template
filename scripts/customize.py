"""Personalize a fresh template checkout using the Python standard library."""
import argparse
import datetime
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def artwork(title, tagline, owner, author, height=420):
    title, tagline, owner, author = map(html.escape, (title, tagline, owner, author))
    offset = (height - 420) // 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{tagline} — by {author}</desc>
<defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="#233149"/></pattern></defs>
<rect width="1280" height="{height}" rx="20" fill="#101827"/>
<rect width="1280" height="{height}" rx="20" fill="url(#grid)" opacity=".45"/>
<g transform="translate(0 {offset})" font-family="DejaVu Sans, Arial, sans-serif">
<rect x="64" y="58" width="36" height="36" rx="10" fill="#89E5CC"/>
<path d="M 73 82 L 82 68 L 91 82 M 77 78 H 87" fill="none" stroke="#101827" stroke-width="2.5"/>
<text x="116" y="82" font-size="15" letter-spacing="2.4" fill="#9CAEC4">{owner.upper()} / OPEN SOURCE</text>
<text x="64" y="191" font-size="51" font-weight="700" letter-spacing="-1.5" fill="#F4F7FB">{title}</text>
<text x="66" y="242" font-size="22" fill="#89E5CC">{tagline}</text>
<path d="M 64 319 H 1216" stroke="#2B3B51"/>
<text x="66" y="360" font-size="16" fill="#9CAEC4">Built by {author}</text>
<text x="1216" y="360" text-anchor="end" font-size="14" fill="#9CAEC4" font-family="DejaVu Sans Mono, monospace">github.com/{owner}</text>
<g transform="translate(1030 90)"><rect width="154" height="154" rx="30" fill="#17263B" stroke="#37516A"/>
<path d="M 61 52 L 36 77 L 61 102 M 93 52 L 118 77 L 93 102 M 86 42 L 68 112" fill="none" stroke="#89E5CC" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="143" cy="12" r="12" fill="#89E5CC"/></g></g></svg>'''


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
    print(f'Customized {args.owner}/{args.repo}. Review README.md; add real installation steps and a demo.')
    print('Export assets/social-preview.svg to PNG, then upload in GitHub Settings → Social preview.')
    print('Run python3 scripts/check.py, then review and commit the changes.')


if __name__ == '__main__':
    main()
