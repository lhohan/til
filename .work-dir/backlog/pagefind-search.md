# Add Pagefind for client-side search

## Why
As the TIL collection grows, full-text search becomes useful. Pagefind is a modern, actively maintained static search library.

## Links
- https://pagefind.app/
- https://github.com/CloudCannon/pagefind

## Implementation notes

1. Install Pagefind (via npm or binary)
2. Run after Zola build: `pagefind --site public`
3. Add to templates:
   ```html
   <link href="/pagefind/pagefind-ui.css" rel="stylesheet">
   <script src="/pagefind/pagefind-ui.js"></script>
   <div id="search"></div>
   <script>
     new PagefindUI({ element: "#search", showSubResults: true });
   </script>
   ```
4. Update GitHub Actions workflow to run Pagefind after `zola build`
5. Update justfile with `pagefind` command

## Acceptance criteria
- [ ] Search input on index page
- [ ] Results show title and snippet
- [ ] Works offline (static)
