# Generate or change your repository banner

The bundled kit comes from [aaitor/assets](https://github.com/aaitor/assets). Read its [complete generation guide](https://github.com/aaitor/assets/blob/c266bc652bc77865d0b1a45b778f3451163a5726/docs/banner-generation.md) for all seven styles, options, and the JavaScript API. The copied source revision is recorded in `shared-assets.json`.

## During project setup

With Python 3.10+ and Node.js 18+ installed:

```bash
python3 scripts/customize.py --repo my-tool --title "My Tool" \
  --tagline "Make everyday work a little easier."
```

This generates `assets/hero.svg` in **diagonal-drift (1a)**, seed `7`, with animation enabled. Optional setup flags:

```text
--banner-style orbit-arcs
--banner-seed 12
--static-banner
```

Setup also updates the README and community files. For subsequent banner edits, use the generator directly rather than rerunning setup with `--force`.

## Regenerate only the banner

From the repository root:

```bash
node banner-kit/make-banner.mjs --style diagonal-drift \
  --repo "My Tool" --tagline "Make everyday work a little easier." \
  --handle "@aaitor" --seed 7 --out assets/hero.svg
```

The generator only replaces the specified SVG. Use `--animate false` for static output. No npm install, account, API key, or network access is required. Existing files are overwritten; ensure the output directory exists.

## List or compare styles

```bash
node banner-kit/make-banner.mjs --list
node banner-kit/make-banner.mjs --all --repo "My Tool" \
  --tagline "Make everyday work a little easier." --out /tmp/my-tool-banners
```

The seven slugs are `diagonal-drift` (1a), `flow-field`, `radial-burst`, `data-streams`, `orbit-arcs`, `signal-waves`, and `circuit-traces`. Pass the slug rather than the design ID. Same seed, options, and source revision produce the same SVG. Colors are defined in `STYLES[slug].colors` in the generator.

## Use the JavaScript API

From the repository root:

```bash
node --input-type=module <<'JS'
import { readFileSync, writeFileSync } from 'node:fs';
import { makeBanner } from './banner-kit/make-banner.mjs';
const svg = makeBanner({
  style: 'diagonal-drift', repo: 'My Tool',
  tagline: 'Make everyday work a little easier.',
  handle: '@aaitor', seed: 7, animate: false,
  fontCss: readFileSync('./banner-kit/fonts.css', 'utf8'),
});
writeFileSync('assets/hero.svg', svg);
JS
```

The API requires explicit `fontCss` to embed fonts and their notices; the CLI loads this automatically. Use a boolean for API `animate` and an integer for `seed`. When calling from Python or another language, pass subprocess arguments as a list instead of interpolating project text into a shell command.

## Preview and share

Open the SVG in a modern browser and check contrast, clipping, and mobile readability. Text does not wrap; keep taglines around 60 characters or fewer. Some SVG viewers do not support embedded fonts or CSS animations, so preview in a browser and use static output or PNG if needed.

The README already embeds `assets/hero.svg`. You can also publish a banner in [aaitor/assets](https://github.com/aaitor/assets) and use a commit-pinned raw URL across repositories. Preserve the bundled [font notices](../banner-kit/NOTICE.md). Banners are 1280 × 320; [social previews](branding.md) remain a separate 1280 × 640 asset.
