# Peter El-Khoury — software engineer portfolio

A responsive portfolio for a senior Java/.NET software engineer, built with plain HTML, CSS, and JavaScript. It includes employer-attributed achievements, six project stories, three detailed case studies and regional CV downloads. No framework, install, build process, paid service, or runtime API is required.

## Preview

Open `index.html` directly, or serve this folder with any static server. For example, with Python installed:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Then open http://127.0.0.1:4173.

## Publish free with GitHub Pages

GitHub Pages supports public repositories on GitHub Free. See [GitHub's Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

Publishing repository: [peterkhoury97/peterelkhoury.github.io](https://github.com/peterkhoury97/peterelkhoury.github.io).

The existing `.github/workflows/static.yml` publishes this site when changes are pushed to **main**. It packages `index.html`, `styles.css`, `script.js`, `.nojekyll`, `robots.txt`, `sitemap.xml`, `assets/`, and `projects/`.

1. Push changes to **main** in the selected repository.
2. In **Settings → Pages**, the source should be **GitHub Actions**.
3. Wait for **Deploy static content to Pages** to succeed in **Actions**.
4. Open the deployment URL reported by the workflow.

For a site at `https://peterkhoury97.github.io`, the repository must be named `peterkhoury97.github.io`. Any other repository name uses a project URL such as `https://peterkhoury97.github.io/portfolio/`.

The selected repository uses the project URL `https://peterkhoury97.github.io/peterelkhoury.github.io/` unless a custom domain is configured.

All image, stylesheet, script, and CV references are relative, so root and project Pages URLs both work. `.nojekyll` keeps this a plain static site. The contact action opens email; there is no backend contact form.

## Edit content

- `index.html`: introduction, projects, career details, skills, contact, and screenshot captions.
- `styles.css`: visual design and responsive layout.
- `script.js`: mobile navigation and accessible screenshot enlargement.
- `assets/images/`: actual project images.
- `assets/Peter-El-Khoury-CV.pdf`: downloadable supplied CV.
- `assets/Peter-El-Khoury-CV-Europe.pdf`, `assets/Peter-El-Khoury-CV-Gulf.pdf`, `assets/Peter-El-Khoury-Resume-Canada.pdf`: two-page regional CV downloads.
- `projects/`: static Pektrix, FreshOps and Peter Personal Trainer case studies.
- `robots.txt`, `sitemap.xml`: public page discovery; update the sitemap when adding pages.
- `docs/screenshot-provenance.md`: source and limitations of every image.

Experience dates match the supplied CV; confirm the current Emcrey role when updating it. The LinkedIn link from the older portfolio was not independently verified and is omitted. Project repositories are not linked until their public URLs are verified.

The portfolio never connects to project databases, scraping services, trading systems, or messaging APIs. Screenshot figures are interface content, not portfolio performance claims.
