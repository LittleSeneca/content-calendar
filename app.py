"""Content Calendar — Markdown-driven content planning."""

import os
import re
import yaml
from datetime import datetime, date, timedelta
from pathlib import Path
from calendar import monthcalendar, month_name

from flask import Flask, render_template, request, redirect, url_for, jsonify
from markdown import markdown

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-me")

CONTENT_DIR = Path(__file__).parent / "content"
CONTENT_DIR.mkdir(exist_ok=True)

# ── Content parsing ──────────────────────────────────────────────

def parse_markdown_file(filepath: Path) -> dict | None:
    """Parse a markdown file with YAML frontmatter. Returns None if no frontmatter."""
    text = filepath.read_text()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    body = parts[2].strip()
    meta["_filename"] = str(filepath.relative_to(CONTENT_DIR))
    meta["_body"] = body
    meta["_body_html"] = markdown(body, extensions=["fenced_code", "tables"])
    return meta


def load_all_posts() -> list[dict]:
    """Load all content items from the content directory."""
    posts = []
    for f in sorted(CONTENT_DIR.rglob("*.md")):
        post = parse_markdown_file(f)
        if post:
            posts.append(post)
    return posts


def post_by_filename(filename: str) -> dict | None:
    """Load a single post by filename."""
    filepath = CONTENT_DIR / filename
    if not filepath.exists():
        return None
    return parse_markdown_file(filepath)


# ── Calendar helpers ──────────────────────────────────────────────

def posts_for_month(year: int, month: int) -> dict[int, list[dict]]:
    """Return posts grouped by day for a given month."""
    posts = load_all_posts()
    by_day: dict[int, list[dict]] = {}
    for p in posts:
        d = p.get("date")
        if not d:
            continue
        if isinstance(d, str):
            d = datetime.strptime(d, "%Y-%m-%d").date()
        if isinstance(d, datetime):
            d = d.date()
        if d.year == year and d.month == month:
            by_day.setdefault(d.day, []).append(p)
    return by_day


def month_nav(year: int, month: int) -> dict:
    """Previous and next month links."""
    prev_month = month - 1
    prev_year = year
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1
    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1
    return {
        "prev": f"/?y={prev_year}&m={prev_month}",
        "next": f"/?y={next_year}&m={next_month}",
    }


# ── Routes ────────────────────────────────────────────────────────

@app.route("/")
def calendar_view():
    today = date.today()
    year = request.args.get("y", today.year, type=int)
    month = request.args.get("m", today.month, type=int)
    month = max(1, min(12, month))

    by_day = posts_for_month(year, month)
    cal = monthcalendar(year, month)
    weeks = []
    for week in cal:
        days = []
        for day in week:
            days.append({
                "day": day,
                "posts": by_day.get(day, []),
                "today": day == today.day and month == today.month and year == today.year,
            })
        weeks.append(days)

    nav = month_nav(year, month)
    return render_template(
        "calendar.html",
        year=year,
        month=month,
        month_name=month_name[month],
        weeks=weeks,
        nav=nav,
        today=today,
    )


@app.route("/list")
def list_view():
    platform = request.args.get("platform", "")
    status = request.args.get("status", "")
    posts = load_all_posts()

    if platform:
        posts = [p for p in posts if p.get("platform", "").lower() == platform.lower()]
    if status:
        posts = [p for p in posts if p.get("status", "").lower() == status.lower()]

    # Sort by date descending
    posts.sort(key=lambda p: str(p.get("date", "")), reverse=True)

    platforms = sorted(set(
        p.get("platform", "") for p in load_all_posts() if p.get("platform")
    ))
    statuses = sorted(set(
        p.get("status", "") for p in load_all_posts() if p.get("status")
    ))

    return render_template(
        "list.html",
        posts=posts,
        platforms=platforms,
        statuses=statuses,
        current_platform=platform,
        current_status=status,
    )


@app.route("/post/<path:filename>")
def view_post(filename):
    post = post_by_filename(filename)
    if not post:
        return "Not found", 404
    return render_template("post.html", post=post)


@app.route("/post/<path:filename>/edit", methods=["GET", "POST"])
def edit_post(filename):
    post = post_by_filename(filename)
    if not post:
        return "Not found", 404

    if request.method == "POST":
        new_title = request.form.get("title", "").strip()
        new_date = request.form.get("date", "").strip()
        new_platform = request.form.get("platform", "").strip()
        new_status = request.form.get("status", "").strip()
        new_tags = request.form.get("tags", "").strip()
        new_scheduled_time = request.form.get("scheduled_time", "").strip()
        new_body = request.form.get("body", "").strip()

        # Rebuild frontmatter
        tags_list = [t.strip() for t in new_tags.split(",") if t.strip()]
        meta = {
            "title": new_title,
            "date": new_date,
            "platform": new_platform,
            "status": new_status,
            "tags": tags_list,
        }
        if new_scheduled_time:
            meta["scheduled_time"] = new_scheduled_time

        content = f"---\n{yaml.dump(meta, default_flow_style=False, allow_unicode=True)}---\n\n{new_body}\n"
        filepath = CONTENT_DIR / filename
        filepath.write_text(content)
        return redirect(url_for("view_post", filename=filename))

    return render_template("editor.html", post=post)


# ── API for Osaka ─────────────────────────────────────────────────

@app.route("/api/posts", methods=["GET"])
def api_list_posts():
    posts = load_all_posts()
    result = []
    for p in posts:
        result.append({
            "title": p.get("title"),
            "date": str(p.get("date", "")),
            "platform": p.get("platform"),
            "status": p.get("status"),
            "tags": p.get("tags", []),
            "filename": p.get("_filename"),
        })
    return jsonify(result)


@app.route("/api/posts", methods=["POST"])
def api_create_post():
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "no data"}), 400

    title = data.get("title", "untitled")
    date_str = data.get("date", date.today().isoformat())
    platform = data.get("platform", "")
    tags = data.get("tags", [])
    status = data.get("status", "draft")
    scheduled_time = data.get("scheduled_time", "")
    body = data.get("body", "")

    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    filename = f"{date_str}-{slug}.md"

    # Auto-route into platform subdirectory, with optional path override
    subpath = data.get("path", "")
    if subpath:
        target_dir = CONTENT_DIR / subpath
    elif platform:
        target_dir = CONTENT_DIR / platform.lower()
    else:
        target_dir = CONTENT_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    filepath = target_dir / filename

    meta = {
        "title": title,
        "date": date_str,
        "platform": platform,
        "status": status,
        "tags": tags,
    }
    if scheduled_time:
        meta["scheduled_time"] = scheduled_time

    content = f"---\n{yaml.dump(meta, default_flow_style=False, allow_unicode=True)}---\n\n{body}\n"
    filepath.write_text(content)

    return jsonify({"ok": True, "filename": filename}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9117, debug=True)
