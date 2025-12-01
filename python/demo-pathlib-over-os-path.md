+++
title = "[DEMO] Prefer pathlib over os.path"
date = 2024-11-10
[taxonomies]
topics = ["python"]
+++

The `pathlib` module (Python 3.4+) provides an object-oriented interface to filesystem paths that's more readable than `os.path`.

```python
from pathlib import Path

# Instead of os.path.join
path = Path("data") / "files" / "output.csv"

# Check existence
if path.exists():
    content = path.read_text()

# Get parts
print(path.stem)      # "output"
print(path.suffix)    # ".csv"
print(path.parent)    # "data/files"

# Glob patterns
for py_file in Path(".").glob("**/*.py"):
    print(py_file)
```

The `/` operator for joining paths is particularly elegant and avoids platform-specific separator issues.
