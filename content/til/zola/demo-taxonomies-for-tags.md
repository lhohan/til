+++
title = "[DEMO] Taxonomies for organizing content"
date = 2024-11-12
[taxonomies]
topics = ["zola"]
+++

Zola's taxonomy system lets you categorize content with tags, categories, or any custom grouping.

In `config.toml`:

```toml
[[taxonomies]]
name = "topics"
feed = true  # Generate RSS for each topic
```

In your content frontmatter:

```toml
[taxonomies]
topics = ["rust", "webdev"]
```

Zola automatically generates:
- `/topics/` - list of all topics
- `/topics/rust/` - all posts tagged "rust"
- `/topics/rust/atom.xml` - RSS feed for "rust" topic

Access in templates:

```jinja2
{% for topic in page.taxonomies.topics %}
  <a href="{{ get_taxonomy_url(kind="topics", name=topic) }}">
    {{ topic }}
  </a>
{% endfor %}
```

You can have multiple taxonomies (tags, categories, series, etc.).
