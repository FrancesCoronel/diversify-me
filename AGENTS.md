# AGENTS.md

Guidance for AI coding agents (Claude Code, Copilot, Codex, and others) working in this repository. Humans should read [CONTRIBUTING.md](CONTRIBUTING.md).

## What this repo is

A list of tech conferences that offer diversity travel grants or scholarships, kept in `README.md`. The GitHub Pages URL ([francescoronel.github.io/diversify-me](https://francescoronel.github.io/diversify-me/)) is only `index.html`, a redirect back to this repo, so all content changes go in `README.md`.

## Adding or updating a conference

- Add one line in the right region section of `README.md`, in alphabetical order:

  ```markdown
  - [Conference Name](https://link-to-scholarship-or-grant-page)
  ```

- Link to the scholarship or travel grant page when one exists, and check that it loads and the grant is still offered.
- Remove entries whose grant no longer exists rather than leaving dead links.
- No trailing whitespace. Don't add conferences without a grant or scholarship.

## Pull requests

- One conference per PR, titled `Add <Conference>`, `Update <Conference>` or `Remove <Conference>`.
- Fill in the PR template, including the checklist. PRs that skip the template may be closed.
- Don't edit workflows or Dependabot config in a list PR.

## Checks

CI comes from the shared workflows in [FrancesCoronel/workflows](https://github.com/FrancesCoronel/workflows) and runs Markdown lint and link checks on every PR.
