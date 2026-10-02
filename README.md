# 🐍 Ali's Python Course

A fun, kid-friendly introduction to Python programming — 10 lessons plus 2 milestone projects, built as a static site with a saved progress tracker.

## What's inside

| | |
|---|---|
| **10 lessons** | from `print()` all the way to `random` & `time` modules |
| **2 milestone projects** | The Secret Agent Mission · The Monster Arena RPG |
| **2 reference sheets** | Snake vs Camel Case · Comparison Operators |
| **Progress bar** | saved in `localStorage` — no login, no backend |

## Progress tracking

Each lesson page has a **Mark This Lesson Complete** button (or press <kbd>C</kbd>).
Completing a page:

- fills the progress bar in the sidebar and the top bar
- ticks the lesson off in the sidebar nav
- fires a confetti celebration
- is remembered the next time you open the site

The bar tracks the 12 curriculum pages (10 lessons + 2 big tasks). The two
reference sheets are bonus material and don't affect the count.

Progress lives in the browser (`localStorage` key `ali-python-course.progress.v1`).
**Reset Progress** in the sidebar clears everything.

## Editing the course

The lesson text is written in Obsidian-flavoured Markdown. To change a lesson,
edit the `.md` file and rebuild:

```bash
python tools/build_site.py
```

Then refresh the browser. The generator handles:

- `[[Wikilinks]]` → real cross-page links
- `> [!tip]` / `[!important]` / `[!caution]` callouts → styled boxes
- fenced code blocks → with one-click **Copy** buttons
- Markdown tables, headings, bold, lists

Adding a whole new lesson means adding one entry to the `COURSE` list at the top
of `tools/build_site.py`.

## Deploying

The site is plain static HTML/CSS/JS with no build step required to host it.

**Cloudflare Pages** — connect this repo and use:

- Framework preset: `None`
- Build command: *(leave empty)*
- Build output directory: `site`

**Any other static host** (Netlify, GitHub Pages, Vercel) — just publish the
`site/` folder.

## Previewing locally

Double-click **`open-course.bat`** (or run `python -m http.server 8000` from
inside `site/`). It serves the site at <http://127.0.0.1:8000> and opens a
browser tab.

That address only works on your own computer — it's a private loopback address,
so nobody else can reach it. To share the course, use the deployed Cloudflare
URL instead.

## How progress behaves

Progress is stored in the browser (`localStorage`), which means it is **per
browser, per device**:

| Scenario | Result |
|---|---|
| Same computer, same browser, returned to later | ✅ Progress kept |
| Different computer, or a different browser | ❌ Starts at 0% |
| Incognito / private window | ❌ Starts at 0%, gone on close |
| "Clear browsing data" including cookies & site data | ❌ Wiped |

Each person browsing the course gets their own separate progress. Nothing is
uploaded anywhere — the site has no backend and no accounts.


## Project layout

```
.
├── *.md                 the course notes (edit these)
├── tools/build_site.py  Markdown → static site generator
└── site/                the generated website  ← deploy this
    ├── index.html       home page with the roadmap
    ├── intro.html
    ├── lesson-1..10.html
    ├── big-task-1..2.html
    ├── snake-case.html
    ├── comparison-operators.html
    └── assets/          style.css · app.js
```
