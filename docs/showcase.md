# Repository design references

A few patterns worth studying, rather than copying entire READMEs. Repositories evolve; these notes reflect the pages reviewed on 2026-10-29. The license of a reference project is independent of this template.

| Repository | Why it works | Apply the pattern |
| --- | --- | --- |
| [Charmbracelet / Gum](https://github.com/charmbracelet/gum) | Distinctive header art, animated terminal demo, tutorial built around actual commands | Give CLI tools personality and show a complete workflow |
| [Browserbase / Stagehand](https://github.com/browserbase/stagehand) | Clear identity, prominent quick-start/docs links, hero, light/dark assets | Make the next useful click obvious for an SDK |
| [Hoppscotch](https://github.com/hoppscotch/hoppscotch) | Recognizable brand, theme-aware banner, product-focused presentation | Show a useful interface or outcome early |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | A direct promise, hero image, very short README, dedicated docs | Keep the README small when comprehensive docs already exist |
| [Astral / uv](https://github.com/astral-sh/uv) | Precise positioning, benchmark graphic, highlights, direct installation paths | Support performance claims with evidence and keep onboarding close |
| [FastAPI](https://github.com/fastapi/fastapi) | Consistent logo, clear positioning, meaningful badges, concrete examples | Use a recognizable identity and practical explanations |

For Aitor's projects: combine Gum's memorable identity, Stagehand's navigation, and uv's concrete onboarding. Use the shared palette and footer, but give every project its own outcome and real demo.

## Review of the supplied research

The [shared ChatGPT research](https://chatgpt.com/share/6ae30167-5ddc-83ed-b6e3-06469abf961d) was reviewed as a source of ideas. This template adopts its MIT default, separate hero/demo assets, consistent personal identity, user-focused README order, community files, and launch discipline.

Adjustments: CI checks real repository behavior instead of displaying placeholder test/coverage badges; setup personalizes links and artwork; no empty source directories or fabricated demos are included. A separate account-level `.github` repository could be added later for inherited community defaults, but creating this template does not change existing projects or account defaults.
