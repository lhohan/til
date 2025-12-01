set shell := ["bash", "-uc"]

dev:
    cd .work-dir && zola serve --drafts

build:
    cd .work-dir && zola build

check:
    cd .work-dir && zola check

update-readme:
    python3 .work-dir/scripts/update-readme.py

clean:
    rm -rf .work-dir/public/
