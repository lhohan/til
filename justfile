set shell := ["bash", "-uc"]

dev: update-readme
    cd .work-dir/site && zola serve --drafts

build: update-readme
    cd .work-dir/site && zola build

check:
    cd .work-dir/site && zola check

new-til topic slug:
    python3 .work-dir/scripts/new_til.py {{topic}} {{slug}}

update-readme:
    python3 .work-dir/scripts/update-readme.py

clean:
    rm -rf .work-dir/site/public/
