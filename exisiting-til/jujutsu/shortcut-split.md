

If you truly need to split an existing commit in place (instead of making a new one), pass the files to `jj split` to keep it non-interactive:

```bash
jj split static/css/main.css
```bash

Note: `split` will always invoke the configured diff editor to let you adjust the commit message; that interaction is part of its design. For a no-editor workflow when committing selected files, stick with [`jj commit -m … <paths>`](./partial-commit,md).
