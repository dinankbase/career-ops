# Fork career-ops to a managed git repo

**Goal:** Turn this plain working copy into a real fork of `santifer/career-ops` so we can selectively pull upstream features without losing our customizations.

**Starting state:**
- Local VERSION: `1.2.0`
- Upstream `main` VERSION: `1.3.0`
- Upstream latest release: `v1.6.0` (2026-04-26)
- No `.git` directory exists yet
- Upstream defaults are Spanish; we have translated + renamed modes to English
- We use a custom `generate-pdf.py` (NOT upstream's Playwright `generate-pdf.mjs`)
- We use the `/browser` skill (NOT Playwright)

## Plan

- [x] 1. `git init` in `F:\Projects\careers`
- [x] 2. Verify `.gitignore` covers personal data (added `inbox/*` — third-party CV PII)
- [x] 3. `git add .` and inspect what's staged before committing
- [x] 4. First commit: `chore: fork from santifer/career-ops v1.2.0 (baseline)` → `c3f71c9`
- [x] 5. Tag the baseline: `git tag fork-base-v1.2.0`
- [x] 6. Add upstream remote: `git remote add upstream https://github.com/santifer/career-ops.git`
- [x] 7. `git fetch upstream` — 152 upstream commits + tags v1.2.0…v1.6.0 fetched
- [ ] 8. **USER**: create empty GitHub repo `<username>/career-ops` (private, no README/license/.gitignore)
- [ ] 9. **USER**: `git remote add origin <url>`
- [ ] 10. **USER**: `git push -u origin main && git push --tags`

## How updates work after this

- `git fetch upstream`
- `git log fork-base-v1.2.0..upstream/main --oneline -- '*.mjs' modes/ templates/` — see what's new
- For features we want: `git checkout upstream/main -- <file>` then commit. Or `git cherry-pick <commit>`.
- **Never run `node update-system.mjs apply`** — it's designed to overwrite system layer wholesale and will clobber our English translations and custom PDF.

## What we are NOT doing

- Not running `update-system.mjs apply`
- Not pulling upstream's `generate-pdf.mjs` (Playwright = bloat, we use `/browser` skill + custom .py)
- Not auto-merging upstream `main` into our branch
- Not yet PR-ing English translations as `modes/en/` (separate decision)
