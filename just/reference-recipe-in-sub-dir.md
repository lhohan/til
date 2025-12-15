# Reference Recipe In Sub Dir

When you have multiple `justfile`s and you want to refer to recipes in a subdirectory you can use modules instead of "`cd`-ing".

Consider

```bash
.
├── bar
│   ├── ...
│   └── justfile
├── ...
└── justfile
```

Reference a `build` recipe from the `justfile` in the subdir:

```just
mod bar

build:
    @just bar::build
```

Also works, what I used to do, but less elegant:

```just
build:
    (cd bar && just build)
```

_Created: 2025-12-15_
