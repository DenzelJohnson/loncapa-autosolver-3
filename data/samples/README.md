# Samples: how to store and name assignment HTML

This folder holds reference HTML pages for assignments so we can reliably test parsing/matching/solving over time.

## Naming convention
- Filename: `assignment_<COURSE>_<ASSIGNMENT>[ _<EXTRA> ].html`
  - Examples:
    - `assignment_1D03_A2.html`
    - `assignment_1D03_A2_2025-09-13.html` (dated variant)
    - `assignment_knight_ch02_hw1.html` (freeform fallback)

- Optional sidecar metadata (same stem, `.meta.json`):
  - `assignment_1D03_A2.meta.json`

Keep everything under `data/samples/` to keep paths short and predictable.

## How to capture from LON-CAPA
1) On the assignment page, right click anywhere on the page
2) Click “Inspect” → go to the “Elements” tab
3) Scroll to the top of the DOM tree
4) Right click the first colored row that starts with `html` (the `<html>` element)
5) Choose “Copy” → “Copy outerHTML”
6) Paste into a new file using the naming convention above (place the file in `data/samples/`)

Tip: ensure you include the entire page (`<html>...</html>`) rather than a snippet.

## Quick HTML template
Create a new file under `data/samples/` and paste the entire page. If you need a placeholder wrapper first, you can start with:

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Assignment Placeholder</title>
</head>
<body>
  <!-- Paste the FULL outerHTML from LON-CAPA here, replacing everything in <body> -->
</body>
</html>
```

Replace the entire `<body>` (or the entire file) with the copied outerHTML.

## Optional metadata template
Create a sidecar JSON file with the same stem (e.g., `assignment_1D03_A2.meta.json`) to store context:

```json
{
  "course": "1D03",
  "assignment": "A2",
  "source_url": "https://.../loncapa/.../assignment",
  "captured_at": "2025-09-13T15:37:00Z",
  "captured_by": "your.name@example.com",
  "notes": "Any quirks in this set, e.g., part order or units",
  "variant": "student-specific or seed id (if applicable)"
}
```

## How to test a stored sample
- From the UI: open `/`, copy the sample file contents and paste into the textarea, then click “Solve Assignment”.
- From the CLI (local):
  - Example:
    ```bash
    PYTHONPATH="$(pwd)" python3 cli.py data/samples/assignment_1D03_A2.html
    ```

## Good practices
- Prefer dated variants only when the same assignment changes often.
- Keep original HTML unmodified. Parser trimming (e.g., removing injected JS snippets) happens in code.
- Use metadata to record any manual context (images, graphs, or what the parts refer to). 