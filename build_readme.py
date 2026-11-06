"""Fill the auto-generated regions of README.md from the GitHub API.

Mirrors the self-updating-profile-readme pattern: each region is delimited by
`<!-- name starts -->` / `<!-- name ends -->` HTML comments, which are invisible
when GitHub renders the page. Regions currently generated:

    releases  - most recent release across all of the user's public repos
    pushed    - most recently pushed public repos, with descriptions

Run with no arguments to rewrite README.md in place:

    python build_readme.py

Set GITHUB_TOKEN to raise the API rate limit (the workflow does this
automatically). Without a token the script still works but may be throttled.
"""

from __future__ import annotations

import os
import pathlib
import re
import sys
import urllib.error
import urllib.request
import json
from datetime import datetime, timezone

USER = "Nathan-W123"
API = "https://api.github.com"
ROOT = pathlib.Path(__file__).parent.resolve()
README = ROOT / "README.md"

# How many entries each column shows.
N_RELEASES = 6
N_PUSHED = 6

# Repos never worth listing: the profile repo itself is noise, and forks are
# not the author's own work.
SKIP_REPOS = {USER.lower(), USER}


def api(path: str) -> list | dict:
    """GET a JSON path from the GitHub API, returning [] on any failure."""
    url = path if path.startswith("http") else f"{API}{path}"
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(f"warning: {url} -> {exc}", file=sys.stderr)
        return []


def _headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-readme",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def own_repos() -> list[dict]:
    """Every public, non-fork, non-archived repo the user owns, newest push first."""
    repos: list[dict] = []
    page = 1
    while True:
        batch = api(f"/users/{USER}/repos?per_page=100&page={page}&sort=pushed")
        if not isinstance(batch, list) or not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [
        r
        for r in repos
        if not r.get("fork")
        and not r.get("archived")
        and not r.get("private")
        and r.get("name") not in SKIP_REPOS
    ]


def fmt_date(stamp: str) -> str:
    """ISO-8601 timestamp -> YYYY-MM-DD, passing anything odd straight through."""
    try:
        return datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return (stamp or "")[:10]


def releases_md(repos: list[dict]) -> str:
    """Latest releases across all repos, most recent first."""
    found: list[tuple[str, str, str, str]] = []
    for repo in repos:
        rels = api(f"/repos/{USER}/{repo['name']}/releases?per_page=5")
        if not isinstance(rels, list):
            continue
        for rel in rels:
            if rel.get("draft"):
                continue
            when = rel.get("published_at") or rel.get("created_at")
            if not when:
                continue
            label = rel.get("name") or rel.get("tag_name") or "release"
            found.append((when, repo["name"], label, rel.get("html_url", "")))

    found.sort(reverse=True)
    if not found:
        return "_No releases published yet._"

    lines = []
    for when, repo, label, url in found[:N_RELEASES]:
        title = label if label.lower().startswith(repo.lower()) else f"{repo} {label}"
        lines.append(f"[{title}]({url}) - {fmt_date(when)}")
    return "\n\n".join(lines)


def pushed_md(repos: list[dict]) -> str:
    """Most recently pushed repos, with their one-line descriptions."""
    if not repos:
        return "_Nothing pushed recently._"

    lines = []
    for repo in repos[:N_PUSHED]:
        desc = (repo.get("description") or "").strip().rstrip(".")
        bullet = f"**[{repo['name']}]({repo['html_url']})** - {fmt_date(repo.get('pushed_at', ''))}"
        if desc:
            bullet += f"<br><sub>{desc}</sub>"
        lines.append(bullet)
    return "\n\n".join(lines)


def replace_region(text: str, name: str, body: str) -> str:
    """Swap the content between `<!-- name starts -->` and `<!-- name ends -->`."""
    pattern = re.compile(
        rf"(<!--\s*{re.escape(name)} starts\s*-->)(.*?)(<!--\s*{re.escape(name)} ends\s*-->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        print(f"warning: no '{name}' region in README.md", file=sys.stderr)
        return text
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main() -> int:
    repos = own_repos()
    print(f"{len(repos)} own public repos", file=sys.stderr)

    text = original = README.read_text(encoding="utf-8")
    text = replace_region(text, "releases", releases_md(repos))
    text = replace_region(text, "pushed", pushed_md(repos))
    text = replace_region(
        text, "updated", f"Updated automatically on {datetime.now(timezone.utc):%Y-%m-%d}."
    )

    if text == original:
        print("README.md unchanged", file=sys.stderr)
        return 0

    README.write_text(text, encoding="utf-8")
    print("README.md updated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
