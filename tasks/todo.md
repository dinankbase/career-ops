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

- [ ] 1. `git init` in `F:\Projects\careers`
- [ ] 2. Verify `.gitignore` covers personal data (cv.md, profile.yml, applications.md, reports/, output/, jds/, inbox/, interview-prep/, data/)
- [ ] 3. `git add .` and inspect what's staged before committing (sanity check no secrets sneak in)
- [ ] 4. First commit: `chore: fork from santifer/career-ops v1.2.0 (baseline)`
- [ ] 5. Tag the baseline: `git tag fork-base-v1.2.0`
- [ ] 6. Add upstream remote: `git remote add upstream https://github.com/santifer/career-ops.git`
- [ ] 7. `git fetch upstream` to make upstream history available locally
- [ ] 8. User creates empty GitHub repo `<username>/career-ops` (private)
- [ ] 9. `git remote add origin git@github.com:<username>/career-ops.git`
- [ ] 10. `git push -u origin main` and `git push --tags`

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
