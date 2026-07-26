#!/usr/bin/env python3
import sys
import re
import requests

def parse_repo_url(url):
    url = url.strip()
    if url.endswith(".git"):
        url = url[:-4]
    patterns = [
        r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$",
        r"^([^/]+)/([^/]+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.groups()
    raise ValueError(f"Could not parse URL: {url}")

def get_readme_raw(owner, repo):
    # Common branch names
    branches = ["main", "master", "develop"]
    # Common README file names (case‑insensitive coverage)
    readme_variants = [
        "README.md", "Readme.md", "readme.md",
        "README.MD", "Readme.MD", "readme.MD",
        "README", "Readme", "readme",
        "README.txt", "Readme.txt", "readme.txt"
    ]
    for branch in branches:
        for name in readme_variants:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{name}"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.text
    raise Exception(f"No README found in common branches/filenames for {owner}/{repo}")

def main():
    print("GitHub README Fetcher (raw URL method)")
    print("---------------------------------------")
    print("Enter repo URLs (one per line, empty line to finish):")
    urls = []
    while True:
        line = input("Repo URL: ").strip()
        if not line:
            break
        urls.append(line)

    repos = []
    for url in urls:
        try:
            owner, repo = parse_repo_url(url)
            repos.append((owner, repo))
        except ValueError as e:
            print(f"⚠️  Skipping: {e}")

    if not repos:
        print("No valid repos.")
        return

    print(f"\nFetching {len(repos)} READMEs...\n")
    with open("readme.txt", "w", encoding="utf-8") as out:
        for idx, (owner, repo) in enumerate(repos):
            print(f"Fetching {owner}/{repo} ... ", end="", flush=True)
            try:
                content = get_readme_raw(owner, repo)
                if idx > 0:
                    out.write("\n\n" + "=" * 80 + "\n\n")
                out.write(f"Repository: https://github.com/{owner}/{repo}\n" + "-" * 40 + "\n\n")
                out.write(content)
                print("✅ Done")
            except Exception as e:
                print(f"❌ Failed: {e}")
                if idx > 0:
                    out.write("\n\n" + "=" * 80 + "\n\n")
                out.write(f"Repository: https://github.com/{owner}/{repo} - ERROR\n{e}\n")

    print("\nSaved to readme.txt")

if __name__ == "__main__":
    main()