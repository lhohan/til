# Enable a GitHub Pages project site from `main` + `/docs`

To host generated static documentation for a project, configure GitHub Pages to **Deploy from a branch** with `main` as the source branch and `/docs` as the source folder.

Steps (GitHub UI):

1. Push your static site files to the repository under `docs/` (entry point is `docs/site/index.html`).
2. In the repository, open **Settings**.
3. In the sidebar, open **Pages**.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Set **Branch** to `main` and **Folder** to `/docs`.
6. Click **Save**.
7. Wait for the Pages deployment to complete (a GitHub Actions workflow starts automatically).
8. Open the site URL.

You can also configure a custom domain in Pages settings.

Official docs:
- [Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Creating a GitHub Pages site](https://docs.github.com/pages/getting-started-with-github-pages/creating-a-github-pages-site)

_Created: 2026-03-06_
