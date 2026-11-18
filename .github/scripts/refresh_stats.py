"""Refresh only the marked statistics in the profile README using GitHub CLI."""

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def github(*args):
    result = subprocess.run(["gh", "api", *args], check=True, capture_output=True)
    return json.loads(result.stdout)


owner = os.environ["GITHUB_REPOSITORY"].split("/")[0]
profile = github(f"users/{owner}")
repositories = github("--paginate", "--slurp", f"users/{owner}/repos?type=owner&per_page=100")
stars = sum(repo["stargazers_count"] for page in repositories for repo in page
            if not repo["private"] and not repo["fork"])
query = """query($login: String!) {
  user(login: $login) { contributionsCollection { contributionCalendar { totalContributions } } }
}"""
data = github("graphql", "-f", f"query={query}", "-f", f"login={owner}")
contributions = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
today = datetime.now(timezone.utc).date()
date_label = f"{today:%B} {today.day}, {today.year}"
stats = (
    f"**{contributions:,}** contributions in the past year · **{profile['public_repos']:,}** public repositories · "
    f"**{stars:,}** stars across original public repositories · **{profile['followers']:,}** followers\n\n"
    f"<sub>Updated {date_label} · Refreshes weekly</sub>"
)

readme = Path("README.md")
original = readme.read_text(encoding="utf-8")
start, end = "<!-- stats:start -->", "<!-- stats:end -->"
if original.count(start) != 1 or original.count(end) != 1 or original.index(start) > original.index(end):
    raise ValueError("Expected one ordered pair of README statistics markers")
before, _, remainder = original.partition(start)
_, _, after = remainder.partition(end)
updated = f"{before}{start}\n{stats}\n{end}{after}"
if updated != original:
    readme.write_text(updated, encoding="utf-8", newline="\n")
