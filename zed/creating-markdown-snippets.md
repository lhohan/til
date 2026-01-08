# Creating Markdown Snippets

A feature that saves a lot of typing, and one I used extensively in IntelliJ, is 'live templates': you type a short text, hit `tab`, and the text expands into whatever you want. In Zed, these are called _snippets_.

You can access and create new snippet types via the `Shift-Cmd-p` shortcut, but I prefer to manage snippets directly in `.config/zed/snippets`. Global snippets can be added to a `snippets.json` file, language-specific ones are added to dedicated files named after the language.

For example, to create snippets for Markdown files, add a `markdown.json` file such as:

```
{
  "Link": {
    "description": "Insert a markdown link",
    "prefix": "link",
    "body": "[${1:link text}](${2:https://example.com})$0",
  },
  "Code block with language": {
    "description": "Insert a syntax-highlighted code block",
    "prefix": "code",
    "body": "```${1:rust}\n$0\n```",
  },
}
```

The `prefix` is what you type to trigger the snippet. `` `${1}` ``, `` `${2}` ``, etc. are placeholders that define tab stops. To present a default value: `` `${1:defaultValue}` ``.
The `` `$0` `` placeholder determines the final cursor position.

Note: extensions are available in Zed for most programming languages. Go to the Extensions menu and search for `snippets`, or browse the dedicated Snippets tab.

_Created: 2026-01-08_
