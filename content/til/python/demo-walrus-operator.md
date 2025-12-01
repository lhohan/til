+++
title = "[DEMO] The walrus operator for assignment expressions"
date = 2024-11-05
[taxonomies]
topics = ["python"]
+++

Python 3.8 introduced the walrus operator `:=` which assigns values as part of an expression.

```python
# Instead of this:
line = input()
while line != "quit":
    process(line)
    line = input()

# You can write:
while (line := input()) != "quit":
    process(line)
```

It's especially useful in list comprehensions with expensive computations:

```python
# Compute once, use twice
results = [y for x in data if (y := expensive(x)) > threshold]
```

And in conditional checks:

```python
if (match := pattern.search(text)):
    print(match.group(0))
```

Use sparingly - readability should come first.
