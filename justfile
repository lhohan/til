set shell := ["bash", "-uc"]

dev:
    zola serve --drafts

build:
    zola build

check:
    zola check

update-readme:
    python3 scripts/update-readme.py

clean:
    rm -rf public/
