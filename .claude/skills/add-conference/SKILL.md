---
name: add-conference
description: Add, update or remove a tech conference with a diversity travel grant or scholarship in the diversify-me README.md list, in the right region and alphabetical order, then run the checks and open a PR. Use when asked to add, update or remove a conference in diversify-me.
---

# Add a conference to diversify-me

1. **Check the grant.** Open the conference's scholarship or travel grant page and confirm it loads and the grant is still offered. No grant or scholarship, no entry. If the grant is gone from an existing entry, remove the entry instead.
2. **Check it's not already listed.** `grep -i "<name or domain>" README.md`. Conferences are sometimes listed under an older name.
3. **Pick the region and sub-group.** Regions are the `## North America` and `## Europe` sections. North America has sub-groups `> USA` and `> Canada`; Europe has none. If nothing fits, stop and ask Frances before adding a region or sub-group.
4. **Add one line** in alphabetical order (ignoring case) within that sub-group, linking the grant page when there is one:

   ```markdown
   - [Conference Name](https://link-to-scholarship-or-grant-page)
   ```

   No trailing whitespace.
5. **Run the checks:**

   ```bash
   npx markdownlint-cli2 README.md
   python3 scripts/check-list.py
   lychee README.md   # if installed
   ```

6. **Open the PR**, one conference per PR, titled `Add <Conference>`, `Update <Conference>` or `Remove <Conference>`. Fill in `.github/PULL_REQUEST_TEMPLATE.md` and leave the Credits item unchecked; agents don't add themselves to Credits. Don't touch workflows or Dependabot config.
