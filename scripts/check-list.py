#!/usr/bin/env python3
"""Check the conference list in README.md.

Within each region (a `## Heading`) and sub-group (a `> USA` style line),
entries must be in alphabetical order, ignoring case. Across the whole list,
no two entries may share a name or a URL.

Usage: python3 scripts/check-list.py [README.md]
Exits 1 and prints each problem when the list has any.
"""

import re
import sys

# `## ` sections that are not regions of the conference list.
NOT_REGIONS = {"Code of Conduct", "Contributing", "Other Resources", "Credits"}

ENTRY = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)\s*$")


def url_key(url):
    """Compare URLs without scheme, leading www. or trailing slash."""
    url = re.sub(r"^https?://", "", url.strip(), flags=re.I)
    url = re.sub(r"^www\.", "", url, flags=re.I)
    host, _, path = url.partition("/")
    return host.lower() + "/" + path.rstrip("/")


def main(path):
    problems = []
    names = {}
    urls = {}
    region = None
    group = None
    prev = None  # (name, line) of the previous entry in this group

    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    for num, line in enumerate(lines, 1):
        if line.startswith("## "):
            title = line[3:].strip()
            region = None if title in NOT_REGIONS else title
            group, prev = None, None
            continue
        if region is None:
            continue
        if line.startswith(">"):
            group, prev = line.lstrip("> ").strip(), None
            continue
        if not line.startswith("- "):
            continue

        where = region + (" > " + group if group else "")
        match = ENTRY.match(line)
        if not match:
            problems.append(f"{path}:{num}: not '- [Name](url)' in {where}: {line}")
            continue
        name, url = match["name"].strip(), match["url"]

        if prev and name.casefold() < prev[0].casefold():
            problems.append(
                f"{path}:{num}: '{name}' should come before '{prev[0]}' "
                f"(line {prev[1]}) in {where}"
            )
        prev = (name, num)

        nkey = name.casefold()
        if nkey in names:
            problems.append(f"{path}:{num}: duplicate name '{name}' (also line {names[nkey]})")
        else:
            names[nkey] = num

        ukey = url_key(url)
        if ukey in urls:
            problems.append(f"{path}:{num}: duplicate URL {url} (also line {urls[ukey]})")
        else:
            urls[ukey] = num

    for problem in problems:
        print(problem)
    if problems:
        return 1
    print(f"{path}: {len(names)} entries OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "README.md"))
