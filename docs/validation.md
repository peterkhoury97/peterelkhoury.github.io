# Portfolio validation

2026-10-07 — local site verification complete.

- Five project cards and five real/source-derived screenshot assets, with provenance and accurate preview labels.
- Responsive checks at 1440, 1024, 768, 360 and 320px: no horizontal overflow.
- All local images load; CV serves a valid PDF.
- Mobile menu opens/closes; Escape restores menu focus.
- Screenshot dialog opens/closes using controls and Escape; focus returns to the triggering link.
- Native project details expand correctly.
- All asset paths work under both root and `/portfolio/` preview URLs.
- All five project stories and navigation remain available with JavaScript disabled.
- Reduced-motion preference disables smooth scrolling and transitions.
- No JavaScript exceptions or failed static resources in browser checks.
- Desktop and mobile screenshots inspected visually; image distortion and tablet overflow corrected.

## Live deployment

Published to the user-selected [peterkhoury97/peterelkhoury.github.io repository](https://github.com/peterkhoury97/peterelkhoury.github.io).

- [GitHub Pages site](https://peterkhoury97.github.io/peterelkhoury.github.io/).
- Deployment commit: `29638c7eb5fb0368017f14d5909af34b4a62a526`.
- [Verified successful Pages run](https://github.com/peterkhoury97/peterelkhoury.github.io/actions/runs/37625197500).
- Live HTML, stylesheet, script, favicon, CV and all five images verified against local content. Text file hashes normalized for Git's Windows/Linux newline conversion; binary assets match exactly.
- Prior repository history preserved. Publishing workflow packages only the site assets, excluding design/research documents.
