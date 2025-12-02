set shell := ["bash", "-uc"]

# Main build task - prepares site and updates README
build-content: _prepare-site _update-readme

# Development server
dev: build-content
    cd .work-dir/site && zola serve --drafts

# Production build
build: build-content
    cd .work-dir/site && zola build

check:
    cd .work-dir/site && zola check

new-til topic slug:
    python3 .work-dir/scripts/new_til.py {{topic}} {{slug}}

# Hidden tasks (prefixed with _ to hide from just --list)
_prepare-site:
    python3 .work-dir/scripts/prepare-site.py

_update-readme:
    python3 .work-dir/scripts/update-readme.py

clean:
    rm -rf .work-dir/site/public/
