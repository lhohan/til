# GitHub: serve pure static content without Jekyll

GitHub Pages build from `main` + `/docs` failed because Jekyll tried to render project markdown files and hit `Liquid syntax error: Unknown tag 'block'`.

Add `docs/.nojekyll` so Pages serves files in `/docs` as static content instead of running Jekyll rendering.

_Created: 2026-03-06_
