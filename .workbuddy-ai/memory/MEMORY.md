# Project notes — Ali's Python Course

## What this project is
A kid-friendly Python course (10 lessons + 2 milestone projects) written by the
user as individual Obsidian Markdown notes at the repo root, plus a generated
static website in `site/` that presents it with progress tracking.

## Conventions
- **Course notes** are the source of truth, at the repo root as `*.md`.
  Names follow `Lesson N -- Title.md` and `Big Task N -- Title.md`.
- The author writes for a child named **Ali** — keep the tone friendly,
  emoji-decorated, and encouraging. Don't strip the emojis from the notes.
- Notes use Obsidian syntax: `[[Wikilinks]]`, `> [!tip]` callouts, `![[images]]`.
- **The site is generated, not hand-edited.** Never edit files in `site/`
  directly — edit the `.md` and re-run `python tools/build_site.py`.

## Rebuild workflow
```bash
# venv already has the `markdown` package
"C:/Users/Ruhul/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe" tools/build_site.py
```

## Deploy target
Cloudflare Pages ← GitHub `learner124-cloud/Python-Course` (public).
Build command: *(empty)* · Output directory: `site`
