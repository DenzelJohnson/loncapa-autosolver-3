## Project scope and structure

```text
loncapa-autosolver-3/
  README.md
  .gitignore
  .env.example
  requirements.txt
  Dockerfile
  render.yaml
  scope.md

  data/
    samples/
      assignment_001.html

  app/
    __init__.py
    main.py                  # web/CLI entrypoint
    pipeline.py              # orchestrates fetch -> parse -> solve
    models.py                # Question, ParsedQuestion, Answer
    navigate.py              # login + navigation + scraping (Playwright)
    pattern_matchers.py      # regex/DOM matchers -> variables/kind
    solution_functions.py    # solver registry + per-kind solvers; includes formatting
    settings.py              # env/config loader
    utils.py                 # misc helpers

    templates/
      index.html

    static/
      app.js
      styles.css

  # Planned (not created yet):
  migrations/                # Alembic revisions
  auth/                      # user accounts & sessions
  payments/                  # Stripe or similar integration
  db/                        # SQLAlchemy models and session
``` 