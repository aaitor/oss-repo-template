# MIT or Apache-2.0?

For personal tools, scripts, CLIs, and skills, use **MIT** as the default. It is short, familiar, and meets the goal of broad reuse. Use **Apache-2.0** when you want an explicit contributor patent grant, especially for SDKs and infrastructure.

| Permission or condition | MIT | Apache-2.0 |
| --- | --- | --- |
| Fork, modify, use privately, use commercially | Yes | Yes |
| Sell or distribute closed-source derivatives | Yes | Yes |
| Must publish modifications or contribute back | No | No |
| Preserve copyright and license notices | Yes | Yes |
| Explicit patent grant and patent-litigation termination | No express clause | Yes |
| Mark changes in redistributed modified files | No general requirement | Yes |
| Preserve relevant upstream NOTICE attribution if supplied | No specific NOTICE mechanism | Yes |

Both licenses have conditions; neither means unrestricted use without retaining notices. Apache-2.0 also expressly excludes trademark permission. Neither license is a requirement to advertise the original author or to keep a marketing footer.

This template uses MIT for original code, documentation, and artwork. Adopters may replace its visible personal branding while retaining the required license and copyright notices. Do not imply endorsement by the original author. Third-party materials keep their own terms. The banner kit embeds Instrument Serif, Geist, and Geist Mono under SIL OFL 1.1; preserve the [bundled font notices](../banner-kit/NOTICE.md).

## Applying your choice

1. Keep a complete license file in each repository. GitHub templates copy files; account-level community defaults do not supply a license.
2. Use the SPDX identifier `MIT` or `Apache-2.0` in package metadata when applicable.
3. For Apache-2.0 projects, use the official unmodified license text and update the README/badge/package metadata together. Follow its application instructions. A separate NOTICE file is not universally required; preserve applicable upstream notices and add your own when appropriate.
4. Verify ownership and dependency compatibility before publishing existing code. A new license does not replace third-party or employer rights.
5. If substantial portions of this MIT template remain, preserve its copyright and permission notice even when your own additions use another license.

Sources: [MIT text and summary](https://choosealicense.com/licenses/mit/), [Apache-2.0 text and summary](https://choosealicense.com/licenses/apache-2.0/), [official Apache application guidance](https://www.apache.org/licenses/LICENSE-2.0).
