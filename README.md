# Peter El-Khoury — software engineer portfolio

A responsive, project-first portfolio built with plain HTML, CSS, and JavaScript. No framework, install, build process, paid service, or runtime API is required.

## Preview

Open `index.html` directly, or serve this folder with any static server. For example, with Python installed:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Then open http://127.0.0.1:4173.

## Publish free with GitHub Pages

GitHub Pages supports public repositories on GitHub Free. See [GitHub's Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

1. Push the site to a public repository on your GitHub account.
2. In that repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select **main** and **/ (root)**, then save.
5. Open the deployment URL shown by GitHub after publishing completes.

For a site at `https://peterkhoury97.github.io`, the repository must be named `peterkhoury97.github.io`. Any other repository name uses a project URL such as `https://peterkhoury97.github.io/portfolio/`.

An existing local portfolio checkout points to `peterkhoury97/peterelkhoury.github.io`; that is a different repository name from the account's user-site repository. Verify the intended destination before updating a live site.

All image, stylesheet, script, and CV references are relative, so root and project Pages URLs both work. `.nojekyll` keeps this a plain static site. The contact action opens email; there is no backend contact form.

## Edit content

- `index.html`: introduction, projects, career details, skills, contact, and screenshot captions.
- `styles.css`: visual design and responsive layout.
- `script.js`: mobile navigation and accessible screenshot enlargement.
- `assets/images/`: actual project images.
- `assets/Peter-El-Khoury-CV.pdf`: downloadable supplied CV.
- `docs/screenshot-provenance.md`: source and limitations of every image.

Experience dates match the supplied CV; confirm the current Emcrey role when updating it. The LinkedIn link from the older portfolio was not independently verified and is omitted. Project repositories are not linked until their public URLs are verified.

The portfolio never connects to project databases, scraping services, trading systems, or messaging APIs. Screenshot figures are interface content, not portfolio performance claims.
