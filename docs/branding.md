# A small visual system

Use a consistent signature across projects: navy `#101827`, mint `#89E5CC`, off-white `#F4F7FB`, muted blue `#9CAEC4`. Keep text high contrast and use one accent. Titles use a sans-serif font; labels use monospace. Original SVG artwork is editable, self-contained, and covered by this repository's MIT license.

## Assets

- `assets/hero.svg`: 1280 × 420 README header. The setup command regenerates the project name and tagline.
- `assets/example-hero.svg`: a fictional project showing the same visual system; not a product demo.
- `assets/social-preview.svg`: 1280 × 640 editable social-card source.
- `assets/social-preview.png`: ready-to-upload social card for this template. Customization removes this PNG because it would show the old project identity.

Keep titles at most 32 characters and taglines at most 76; use a concise outcome. Check the result at mobile width. If a translation or a long name needs more space, edit the SVG text size/layout.

## Export a personalized social card

With CairoSVG installed in an isolated environment, run from the repository root:

```bash
python3 -m venv .venv
.venv/bin/pip install cairosvg
.venv/bin/cairosvg assets/social-preview.svg -o assets/social-preview.png
```

Alternatively export the SVG to PNG in a vector editor. The PNG should be under 1 MB. In GitHub, open **Settings → General → Social preview → Edit → Upload an image**. Merely committing the image does not configure the repository preview. Template generation does not copy repository settings; set the preview on each new repo.

[GitHub recommends 1280 × 640 for best display](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

## Demo media

Place a real screenshot, small GIF/WebP, or terminal recording after the introduction. Give it descriptive alt text, sample input, and expected output. Avoid autoplay, large files, fake benchmarks, and unreadable full-screen captures. The hero establishes identity; the demo shows the software working.

Use a short author footer linking to the maintainer profile. Adopters may replace the name, colors, and artwork; preserve required license notices.
