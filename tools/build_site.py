#!/usr/bin/env python3
# ============================================================
#  Ali's Python Course — static site builder
#  Reads the Obsidian .md notes and emits a static site into ./site
#
#  Usage:  python tools/build_site.py
# ============================================================

import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"

# ------------------------------------------------------------
# Course roadmap.  "order" is the canonical completion order
# used by the progress bar.  `slug` becomes the output filename.
# ------------------------------------------------------------

COURSE = [
    # ---- intro (part 0) ----
    dict(slug="intro", src="Introduction to Python.md", title="Introduction to Python",
         nav="Intro & Roadmap", part=0, kind="intro", id="intro",
         desc="Start here! What Python is, how this course works, and your full roadmap."),

    # ---- Part 1 ----
    dict(slug="lesson-1", src="Lesson 1 -- Basics Of Python.md", title="Basics Of Python",
         nav="Basics Of Python", part=1, kind="lesson", num=1, id="lesson-1",
         desc="Print, data types, variables and maths superpowers."),
    dict(slug="lesson-2", src="Lesson 2 -- Talking to Python with Input.md", title="Talking to Python with Input",
         nav="Talking to Python with Input", part=1, kind="lesson", num=2, id="lesson-2",
         desc="Make Python listen with input() and talk back with f-strings."),
    dict(slug="lesson-3", src="Lesson 3 -- Making Decisions with If and Else.md", title="Making Decisions with If and Else",
         nav="Making Decisions (If / Else)", part=1, kind="lesson", num=3, id="lesson-3",
         desc="Give your code a brain so it can choose what to do."),
    dict(slug="lesson-4", src="Lesson 4 -- Logic and Secret Passwords.md", title="Logic and Secret Passwords",
         nav="Logic and Secret Passwords", part=1, kind="lesson", num=4, id="lesson-4",
         desc="Unlock secret doors with and, or and not."),
    dict(slug="lesson-5", src="Lesson 5 -- For Loops and Repeating Magic.md", title="For Loops and Repeating Magic",
         nav="For Loops & Repeating Magic", part=1, kind="lesson", num=5, id="lesson-5",
         desc="Repeat actions effortlessly by casting loop spells."),
    dict(slug="big-task-1", src="Big Task 1 -- The Secret Agent Mission.md", title="The Secret Agent Mission",
         nav="BIG TASK 1: Secret Agent", part=1, kind="bigtask", id="big-task-1",
         desc="🏆 Mini-project #1 — combine lessons 1–5 into a real game."),

    # ---- Part 2 ----
    dict(slug="lesson-6", src="Lesson 6 -- While Loops and Game Loops.md", title="While Loops and Game Loops",
         nav="While Loops & Game Loops", part=2, kind="lesson", num=6, id="lesson-6",
         desc="Build game loops that keep running until you win."),
    dict(slug="lesson-7", src="Lesson 7 -- Lists -- The Super Backpack.md", title="Lists -- The Super Backpack",
         nav="Lists: The Super Backpack", part=2, kind="lesson", num=7, id="lesson-7",
         desc="Store an entire inventory of items in one variable."),
    dict(slug="lesson-8", src="Lesson 8 -- Looping Through Lists.md", title="Looping Through Lists",
         nav="Looping Through Lists", part=2, kind="lesson", num=8, id="lesson-8",
         desc="Scan your backpack and hunt for rare treasures."),
    dict(slug="lesson-9", src="Lesson 9 -- Functions -- Your Custom Superpowers.md", title="Functions -- Your Custom Superpowers",
         nav="Functions: Custom Superpowers", part=2, kind="lesson", num=9, id="lesson-9",
         desc="Invent your own reusable code superpowers with def."),
    dict(slug="lesson-10", src="Lesson 10 -- Modules and Random Adventures.md", title="Modules and Random Adventures",
         nav="Modules & Random Adventures", part=2, kind="lesson", num=10, id="lesson-10",
         desc="Add dice rolls, random loot and dramatic pauses."),
    dict(slug="big-task-2", src="Big Task 2 -- The Monster Arena RPG.md", title="The Monster Arena RPG",
         nav="BIG TASK 2: Monster Arena", part=2, kind="bigtask", id="big-task-2",
         desc="👑 Final boss project — build a full turn-based RPG!"),

    # ---- extras (reference pages, count toward progress too) ----
    dict(slug="snake-case", src="Snake Case or Camel Case.md", title="Snake Case or Camel Case?",
         nav="Snake Case or Camel Case", part=3, kind="extra", id="snake-case",
         desc="Two styles for naming variables — and Python's favourite."),
    dict(slug="comparison-operators", src="Comparison Operators in Python.md", title="Comparison Operators in Python",
         nav="Comparison Operators", part=3, kind="extra", id="comparison-operators",
         desc="The 6 symbols Python uses to compare things."),
]

PARTS = {
    0: dict(name="Getting Started", pill="Start"),
    1: dict(name="Python Super-Agent Basics", pill="Part 1"),
    2: dict(name="Lists, Functions & Game Creation", pill="Part 2"),
    3: dict(name="Bonus Reference Sheets", pill="Extras"),
}

# progress bar only counts the main curriculum (lessons + big tasks)
TRACKED = {c["id"] for c in COURSE if c["kind"] in ("lesson", "bigtask")}


# ------------------------------------------------------------
# Cross-reference resolution  ([[Wikilinks]])
# ------------------------------------------------------------

# every source filename (with and without .md) -> entry
SRC_INDEX = {}
for c in COURSE:
    SRC_INDEX[c["src"]] = c
    SRC_INDEX[c["src"][:-3]] = c
    SRC_INDEX[c["src"].replace(" -- ", " - ")] = c
    SRC_INDEX[c["src"][:-3].replace(" -- ", " - ")] = c
    SRC_INDEX[c["title"]] = c


def resolve(target: str):
    """Return the course entry for a wikilink target, or None."""
    t = target.strip()
    if t in SRC_INDEX:
        return SRC_INDEX[t]

    def norm(s):
        return re.sub(r"[^a-z0-9]+", "", s.lower())

    nt = norm(t)
    if not nt:
        return None
    # exact normalised match first
    for key, entry in SRC_INDEX.items():
        if norm(key) == nt:
            return entry
    # then prefix / containment
    for key, entry in SRC_INDEX.items():
        if nt.startswith(norm(key)) or norm(key).startswith(nt):
            if len(nt) >= 5:
                return entry
    return None


def obsidian_md_tweaks(text: str) -> str:
    """
    Obsidian is lenient about blank lines before lists / headings; plain
    Python-Markdown is not. Without a blank line, a list right after a
    paragraph collapses into the paragraph. Insert the missing separator.
    """
    lines = text.split("\n")
    out = []
    in_fence = False
    list_re = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")
    head_re = re.compile(r"^\s{0,3}#{1,6}\s")
    table_re = re.compile(r"^\s*\|.*\|\s*$")

    for idx, line in enumerate(lines):
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        is_block_start = bool(list_re.match(line) or head_re.match(line) or table_re.match(line))

        if is_block_start and out:
            prev = out[-1]
            prev_stripped = prev.strip()
            prev_is_block = bool(
                prev_stripped == ""
                or list_re.match(prev)
                or head_re.match(prev)
                or table_re.match(prev)
                or prev_stripped.startswith(">")
                or prev_stripped.startswith("```")
            )
            # a list may directly follow another list line (continuation)
            prev_is_list = bool(list_re.match(prev))
            cur_is_list = bool(list_re.match(line))
            if not prev_is_block and not (prev_is_list and cur_is_list):
                out.append("")

        out.append(line)

    return "\n".join(out)


WIKILINK_RE = re.compile(r"\[\[([^\]\|]+?)(?:\|([^\]]+?))?\]\]")


def replace_wikilinks(text: str) -> str:
    def sub(m):
        target, alias = m.group(1), m.group(2)
        entry = resolve(target)
        label = (alias or target).strip()
        if entry:
            return (
                f'<a class="wikilink" href="{entry["slug"]}.html" '
                f'data-wikilink="{html.escape(target)}">{html.escape(label)}</a>'
            )
        return f'<a class="wikilink" href="#">{html.escape(label)}</a>'  # unresolved (dead)

    return WIKILINK_RE.sub(sub, text)


IMG_RE = re.compile(r"!\[\[([^\]]+?)\]\]")


def replace_images(text: str) -> str:
    """Obsidian embeds. We don't ship the pasted PNGs, so degrade gracefully."""

    def sub(m):
        name = m.group(1)
        return (
            '<span class="img-missing" title="Image not bundled with the site">'
            f"\U0001f5bc\ufe0f {html.escape(name)}"
            "</span>"
        )

    return IMG_RE.sub(sub, text)


# ------------------------------------------------------------
# Markdown pipeline
# ------------------------------------------------------------

MD = markdown.Markdown(
    extensions=[
        "fenced_code",
        "tables",
        "attr_list",
        "md_in_html",
        "sane_lists",
    ],
    output_format="html5",
)

CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\]([+-]?)\s*(.*)$")
QUOTE_RE = re.compile(r"^>\s?(.*)$")

TITLES = {
    "tip": "\U0001f4a1 Tip",
    "important": "\u26a0\ufe0f Important",
    "caution": "\U0001f9f1 Caution",
    "warning": "\u26a0\ufe0f Warning",
    "note": "\U0001f4cc Note",
    "example": "\U0001f4bb Example",
    "quote": "Quote",
    "info": "\u2139\ufe0f Info",
    "abstract": "\U0001f4d8 Summary",
    "question": "\u2753 Question",
    "success": "\u2705 Success",
    "danger": "\U0001f525 Danger",
}


def convert_callouts(text: str) -> str:
    """Turn Obsidian > [!tip] blocks into <div class="callout"> HTML."""
    lines = text.split("\n")
    out, i = [], 0

    while i < len(lines):
        m = CALLOUT_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        kind = m.group(1).lower()
        custom = m.group(3).strip()
        type_title = TITLES.get(kind, "\U0001f4cc " + kind.capitalize())
        title = f"{type_title} &mdash; {custom}" if custom else type_title

        body_lines = []
        i += 1
        while i < len(lines):
            qm = QUOTE_RE.match(lines[i])
            if qm:
                body_lines.append(qm.group(1))
                i += 1
            elif lines[i].strip() == "":
                # blank line: keep it only if the quote continues after it
                j = i + 1
                if j < len(lines) and QUOTE_RE.match(lines[j]):
                    body_lines.append("")
                    i += 1
                else:
                    break
            else:
                break

        body_md = "\n".join(body_lines).strip()
        MD.reset()
        body_html = MD.convert(replace_wikilinks(replace_images(body_md)))

        out.append(
            f'<div class="callout {kind}">'
            f'<div class="callout-head">{title}</div>'
            f'<div class="callout-body">{body_html}</div>'
            f"</div>"
        )

    return "\n".join(out)


def md_to_html(text: str) -> str:
    text = replace_images(text)
    text = replace_wikilinks(text)
    text = convert_callouts(text)
    text = obsidian_md_tweaks(text)
    MD.reset()
    return MD.convert(text)


# ------------------------------------------------------------
# Post-processing of rendered HTML
# ------------------------------------------------------------

CODE_RE = re.compile(r"<pre><code(?: class=\"([^\"]*)\")?>(.*?)</code></pre>", re.S)


def style_code_blocks(body: str) -> str:
    def sub(m):
        cls = m.group(1) or ""
        code = m.group(2)
        lang = ""
        m2 = re.search(r"language-(\w+)", cls)
        if m2:
            lang = m2.group(1)
        is_console = lang in ("text", "console", "bash", "shell")
        return (
            f'<div class="code-block{" console" if is_console else ""}">'
            f'<div class="code-head">'
            f'<span class="dots"><i></i><i></i><i></i></span>'
            f'<span class="code-lang">{html.escape(lang or "code")}</span>'
            f'<span class="spacer"></span>'
            f'<button class="copy-btn" type="button">Copy</button>'
            f"</div>"
            f"<pre>{code}</pre>"
            f"</div>"
        )

    return CODE_RE.sub(sub, body)


def wrap_tables(body: str) -> str:
    return body.replace("<table>", '<div class="table-scroll"><table>').replace(
        "</table>", "</table></div>"
    )


def strip_obsidian_nav(text: str) -> str:
    """Remove the hand-written prev/next lines & leading rule from the notes."""
    lines = text.split("\n")
    cleaned = []
    for ln in lines:
        s = ln.strip()
        # lines that are basically just two wikilinks + arrows
        if s.count("[[") >= 1 and s.count("]]") >= 1 and len(
            re.sub(r"\[\[[^\]]*\]\]", "", s).replace("|", "").strip(" \u2b05\ufe0f\u27a1\ufe0f-—~ ")
        ) <= 8:
            continue
        cleaned.append(ln)
    return "\n".join(cleaned)


def strip_leading_rule(text: str) -> str:
    lines = text.split("\n")
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[0].strip() in ("---", "***", "___"):
        lines.pop(0)
        while lines and lines[0].strip() == "":
            lines.pop(0)
    return "\n".join(lines)


def drop_leading_h1(text: str) -> str:
    """
    The notes each open with their own `# Lesson 7: ...` heading (or an
    emoji-decorated variant). We render our own <h1> from the roadmap, so
    drop the note's leading H1 to avoid showing the title twice.
    Only strips it when it is the very first block of the document.
    """
    lines = text.split("\n")
    out = []
    stripped_once = False

    for line in lines:
        if not stripped_once and line.strip() == "":
            out.append(line)
            continue
        if not stripped_once and re.match(r"^\s*#\s+\S", line):
            stripped_once = True
            continue
        out.append(line)

    return "\n".join(out)


# ------------------------------------------------------------
# Page shell
# ------------------------------------------------------------

def nav_html(current_id: str) -> str:
    """Sidebar nav grouped by part."""
    chunks = []

    for pnum in (0, 1, 2, 3):
        items = [c for c in COURSE if c["part"] == pnum]
        if not items:
            continue
        info = PARTS[pnum]
        chunks.append(f'<div class="nav-part">{html.escape(info["name"])}</div>')
        chunks.append('<ul class="nav-list">')

        for c in items:
            active = " active" if c["id"] == current_id else ""
            milestone = " milestone" if c["kind"] == "bigtask" else ""
            # visual marker: big tasks get a crown/star instead of a number
            if c["kind"] == "bigtask":
                num = "\u2b50" if "1" in c["id"] else "\U0001f451"
            elif c["kind"] == "lesson":
                num = str(c["num"])
            elif c["kind"] == "intro":
                num = "\U0001f3e0"
            else:
                num = "\U0001f4d8"

            tracked = "1" if c["id"] in TRACKED else "0"
            chunks.append(
                f'<li><a class="nav-item{milestone}{active}" href="{c["slug"]}.html" '
                f'data-id="{c["id"]}" data-label="{html.escape(c["nav"])}" '
                f'data-tracked="{tracked}" title="{html.escape(c["nav"])}">'
                f'<span class="nav-dot"></span>'
                f'<span class="nav-num">{num}</span>'
                f'<span class="nav-label">{html.escape(c["nav"])}</span>'
                f"</a></li>"
            )
        chunks.append("</ul>")

    return "\n".join(chunks)


def page(title: str, body: str, current_id: str, wide: bool = False) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} &middot; Ali's Python Course</title>
<meta name="description" content="Ali's Python Course - a fun, kid-friendly introduction to Python programming.">
<meta name="color-scheme" content="dark">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#128013;</text></svg>">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="layout">

  <aside class="sidebar">
    <a class="brand" href="index.html">
      <div class="brand-title">&#128013; Ali's Python Course</div>
      <div class="brand-sub">Beginner &rarr; Game Coder</div>
    </a>

    <div class="progress-card">
      <div class="progress-head">
        <span class="label">Your Progress</span>
        <span class="pct" id="sb-pct">0%</span>
      </div>
      <div class="bar"><span id="sb-bar"></span></div>
      <div class="progress-foot">
        <span id="sb-count">0 / 0 lessons</span>
        <span class="cheer" id="sb-cheer">Ready to start!</span>
      </div>
    </div>

    <nav>{nav_html(current_id)}</nav>

    <div class="sidebar-actions">
      <button type="button" id="reset-btn" class="danger">Reset Progress</button>
    </div>
  </aside>

  <main class="main">
    <div class="topbar">
      <button type="button" class="menu-btn" id="menu-btn" aria-label="Toggle menu">&#9776;</button>
      <div class="mini-bar">
        <span class="mini-label">Progress</span>
        <div class="bar"><span id="mb-bar"></span></div>
        <span id="mb-txt">0%</span>
      </div>
      <span class="spacer"></span>
      <a class="btn ghost" href="index.html">&#127968; Home</a>
    </div>

    <div class="wrap{" wide" if wide else ""}">
{body}
    </div>
  </main>
</div>

<div class="toast" id="toast"></div>
<script src="assets/app.js"></script>
</body>
</html>
"""


# ------------------------------------------------------------
# Home page
# ------------------------------------------------------------

def build_home() -> str:
    parts = []

    for pnum in (0, 1, 2, 3):
        items = [c for c in COURSE if c["part"] == pnum]
        if not items:
            continue
        info = PARTS[pnum]

        cards = []
        for c in items:
            if c["kind"] == "bigtask":
                num = "\U0001f3c6" if "1" in c["id"] else "\U0001f451"
                tag = "Big Task"
            elif c["kind"] == "lesson":
                num = str(c["num"])
                tag = "Lesson"
            elif c["kind"] == "intro":
                num = "\U0001f3e0"
                tag = "Start"
            else:
                num = "\U0001f4d8"
                tag = "Reference"

            milestone = " milestone" if c["kind"] == "bigtask" else ""
            cards.append(
                f'<a class="card{milestone}" href="{c["slug"]}.html" data-id="{c["id"]}">'
                f'<div class="card-top"><span class="num">{num}</span>'
                f'<span class="tag">{tag}</span></div>'
                f'<h3>{html.escape(c["title"])}</h3>'
                f'<div class="desc">{html.escape(c["desc"])}</div>'
                f'<div class="state">Start lesson &rarr;</div>'
                f"</a>"
            )

        parts.append(
            f'<section class="part-block">'
            f'<div class="part-head">'
            f'<span class="pill">{html.escape(info["pill"])}</span>'
            f'<h2>{html.escape(info["name"])}</h2>'
            f'<span class="count">{len(items)} pages</span>'
            f"</div>"
            f'<div class="cards">{"".join(cards)}</div>'
            f"</section>"
        )

    body = f"""
<div class="hero">
  <span class="kicker">Welcome aboard, Ali!</span>
  <h1>&#128013; Become a Python Code Master</h1>
  <p class="lede">
    A 10-lesson adventure that starts with a single <code>print()</code> and ends with
    you building your own turn-based <strong>Monster Arena RPG</strong>.
    Tick off each lesson as you finish it and watch your progress bar climb.
  </p>

  <div class="hero-progress">
    <div class="row1">
      <span class="big" id="hero-pct">0%</span>
      <span class="sub" id="hero-row2-count">0 of 0 lessons complete</span>
    </div>
    <div class="bar"><span id="hero-bar"></span></div>
    <div class="row2">
      <span>Up next: <a class="wikilink" id="hero-next" href="lesson-1.html">Basics Of Python</a></span>
      <span>&#128161; Press <strong>C</strong> to complete a lesson</span>
    </div>
  </div>
</div>

{''.join(parts)}

<div class="finish-note" id="finish-banner" style="display:none;border-style:solid;border-color:#2b5a35;color:#3fb950;">
  &#127942; <strong>All lessons complete!</strong> You have officially finished the whole Python course. Time to build something amazing!
</div>

<div class="finish-note">
  Your progress is saved automatically in this browser &mdash; no account needed.
</div>
"""
    return page("Home", body, "", wide=True)


# ------------------------------------------------------------
# Lesson pages
# ------------------------------------------------------------

def pager_html(idx: int) -> str:
    prev_c = COURSE[idx - 1] if idx > 0 else None
    next_c = COURSE[idx + 1] if idx + 1 < len(COURSE) else None

    left = (
        f'<a class="prev" href="{prev_c["slug"]}.html">'
        f'<span class="dir">&larr; Previous</span>'
        f'<span class="nm">{html.escape(prev_c["nav"])}</span></a>'
        if prev_c else
        '<a class="prev disabled"><span class="dir">&larr; Previous</span>'
        '<span class="nm">You are at the start</span></a>'
    )
    right = (
        f'<a class="next" href="{next_c["slug"]}.html">'
        f'<span class="dir">Next &rarr;</span>'
        f'<span class="nm">{html.escape(next_c["nav"])}</span></a>'
        if next_c else
        '<a class="next disabled"><span class="dir">Next &rarr;</span>'
        '<span class="nm">Course complete!</span></a>'
    )
    return f'<div class="pager">{left}{right}</div>'


def build_lesson(entry: dict, idx: int) -> str:
    raw = (ROOT / entry["src"]).read_text(encoding="utf-8")
    text = strip_leading_rule(raw)
    text = strip_obsidian_nav(text)

    # Drop the note's own leading H1 (we render a cleaner title ourselves).
    text = drop_leading_h1(text)

    inner = style_code_blocks(wrap_tables(md_to_html(text)))

    kind_label = {
        "lesson": "Lesson", "bigtask": "Milestone Project",
        "intro": "Start Here", "extra": "Reference Sheet",
    }[entry["kind"]]

    body = f"""
<div class="crumb">
  <a href="index.html">Home</a> &nbsp;/&nbsp; {html.escape(PARTS[entry["part"]]["name"])}
  &nbsp;/&nbsp; {html.escape(kind_label)}
</div>

<article>
  <h1>{html.escape(entry["title"])}</h1>
{inner}
</article>

<div class="lesson-foot">
  <div class="complete-row">
    <div class="txt">
      <div class="t1">Finished this one?</div>
      <div class="t2">Mark it complete and your progress bar will jump up. You can undo this any time.</div>
    </div>
    <button class="btn primary" type="button" id="complete-btn"
            data-id="{entry["id"]}" aria-pressed="false">
      <span>&#11088;</span> Mark This Lesson Complete
    </button>
  </div>
  {pager_html(idx)}
</div>
"""
    return page(entry["title"], body, entry["id"])


# ------------------------------------------------------------
# Build
# ------------------------------------------------------------

def main() -> int:
    OUT.mkdir(exist_ok=True)

    missing = [c["src"] for c in COURSE if not (ROOT / c["src"]).exists()]
    if missing:
        print("ERROR: missing source files:")
        for m in missing:
            print("  -", m)
        return 1

    (OUT / "index.html").write_text(build_home(), encoding="utf-8")

    for idx, entry in enumerate(COURSE):
        # Every entry gets its own page. Note: the intro lives at
        # `intro.html` precisely so it does NOT clobber the home page.
        html_out = build_lesson(entry, idx)
        (OUT / (entry["slug"] + ".html")).write_text(html_out, encoding="utf-8")

    # write a manifest so other tools / deployments know the order
    (OUT / "course-manifest.json").write_text(
        json.dumps(
            {
                "title": "Ali's Python Course",
                "tracked": sorted(TRACKED),
                "pages": [
                    {
                        "id": c["id"], "slug": c["slug"], "title": c["title"],
                        "part": c["part"], "kind": c["kind"],
                        "tracked": c["id"] in TRACKED,
                    }
                    for c in COURSE
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Built {len(COURSE) + 1} pages into {OUT}")
    checked = sum(1 for _ in OUT.glob("*.html"))
    print(f"HTML files: {checked}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
