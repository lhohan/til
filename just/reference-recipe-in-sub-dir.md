# Reference Recipe In Sub Dir

When you have multiple `justfile`s in a nested directory structure and you want to refer to recipes in a subdirectory, you can use modules instead of changing directory.

Consider

```bash
.
├── bar
│   ├── ...
│   └── justfile
├── ...
└── justfile
```

To reference a `build` recipe from the `justfile` in the subdirectory:

```bash
mod bar

build:
    @just bar::build
```

The following also works (what I used to do), but it's less elegant:

```bash
build:
    (cd bar && just build)
```

_Created: 2025-12-15_
