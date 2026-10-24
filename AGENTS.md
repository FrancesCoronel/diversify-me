# AGENTS.md

Guidance for AI coding agents (Claude Code, Copilot, Codex, and others) working in this repository. Humans should read [CONTRIBUTING.md](CONTRIBUTING.md).

## What this repo is

A list of tech conferences that offer diversity travel grants or scholarships, kept in `README.md`. The GitHub Pages URL ([francescoronel.github.io/diversify-me](https://francescoronel.github.io/diversify-me/)) is only `index.html`, a redirect back to this repo, so all content changes go in `README.md`.

## How the list is organized

- The list is the `## North America` and `## Europe` sections of `README.md`. The `##` sections after them (Code of Conduct, Contributing, Other Resources, Credits) are not part of the list.
- A region can have sub-groups, each a blockquote line followed by its entries: North America has `> USA` and `> Canada`; Europe has none.
- Alphabetical order (ignoring case) applies within each sub-group, or within the region when it has no sub-groups.
- If a conference fits no existing region or sub-group, ask Frances before adding a new one.

## Adding or updating a conference

- Add one line in the right region or sub-group of `README.md`, in alphabetical order:

  ```markdown
  - [Conference Name](https://link-to-scholarship-or-grant-page)
  ```

- Link to the scholarship or travel grant page when one exists, and check that it loads and the grant is still offered.
- Remove entries whose grant no longer exists rather than leaving dead links.
- No trailing whitespace. Don't add conferences without a grant or scholarship.

## Pull requests

- One conference per PR, titled `Add <Conference>`, `Update <Conference>` or `Remove <Conference>`.
- Fill in the PR template, including the checklist. PRs that skip the template may be closed.
- Agents don't add themselves to the Credits list in `README.md`; leave that checklist item unchecked.
- Don't edit workflows or Dependabot config in a list PR.

## Checks

CI comes from the shared workflows in [FrancesCoronel/workflows](https://github.com/FrancesCoronel/workflows) and runs Markdown lint and link checks on every PR.

Run these before opening a PR:

```bash
npx markdownlint-cli2 README.md   # uses .markdownlint.json, same as CI
python3 scripts/check-list.py     # alphabetical within each sub-group, no duplicate names or URLs
lychee README.md                  # if lychee is installed; honors .lycheeignore
```

`scripts/check-list.py` doesn't run in CI yet, so run it yourself. The `add-conference` skill (`.claude/skills/add-conference/`) walks through adding an entry.
