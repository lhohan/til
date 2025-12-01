+++
title = "Shortcodes for reusable embeds"
date = 2024-11-22
[taxonomies]
topics = ["zola"]
+++

Zola shortcodes let you create reusable components that can be used in Markdown content.

Create `templates/shortcodes/youtube.html`:

```html
<div class="video-embed">
  <iframe 
    src="https://www.youtube.com/embed/{{ id }}"
    frameborder="0"
    allowfullscreen>
  </iframe>
</div>
```

Use in Markdown:

```markdown
Check out this video:

{{/* youtube(id="dQw4w9WgXcQ") */}}
```

Shortcodes can also wrap content:

```html
<!-- templates/shortcodes/note.html -->
<div class="note note-{{ type | default(value="info") }}">
  {{ body }}
</div>
```

```markdown
{%/* note(type="warning") */%}
This is important!
{%/* end */%}
```
