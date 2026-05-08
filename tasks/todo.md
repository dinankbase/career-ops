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

---

# Application phase — top 7 shortlist (2026-04-27)

**Goal:** Apply to the 7 shortlisted roles (score ≥ 4.0) from today's batch evaluation. Each application gets a tailored CV PDF, drafted form answers, and a final review by operator before Submit.

**Source of evaluations:** `reports/014` through `reports/029` (full A-G in each). Tracker rows in `data/applications.md` #11-#30. Pipeline already moved to Processed.

## Top 7 shortlist (in score order)

| # | Score | Company | Role | URL | Comp | Hook |
|---|-------|---------|------|-----|------|------|
| 022 | 4.6 | VisCap Media | UGC Creative Strategist (US Remote) | https://www.linkedin.com/jobs/view/4403780305/ | TBD | ComfyUI + improv + 10y photography. Named hiring manager identified |
| 019 | 4.5 | RemodelBoom | Performance Creative Strategist (US Remote) | https://www.linkedin.com/jobs/view/4402624682/ | $96K base + uncapped ROAS bonus | JD names Halbert/Schwartz/Ogilvy. DR canon match |
| 015 | 4.4 | Kāsper | Junior Creative Strategist (Toronto Remote) | https://www.linkedin.com/jobs/view/4405681245/ | $55-70K CAD | Junior level matches; geo match; easiest first apply |
| 024 | 4.4 | AJ Media | Direct Response Copywriter & CRO (US Remote) | https://www.linkedin.com/jobs/view/4404093768/ | Listed $3-4K/yr (typo, confirm) | Best-shaped role: copy + analytical hybrid. Apply via trial pitch |
| 018 | 4.1 | Odyssey | Creative Strategist (US Remote) | https://www.linkedin.com/jobs/view/4405463857/ | $75-115K USD | Loom video required — sales-presentation strength |
| 017 | 4.0 | Publish Experts | Creative Strategist (US Remote) | https://www.linkedin.com/jobs/view/4404717180/ | TBD | Kennedy/Brunson named. Paid trial structure |
| 027 | 4.0 | GLP Winner | Performance Creative + Graphic Design + Strategy (US Remote) | https://www.linkedin.com/jobs/view/4403504374/ | TBD | Portfolio-judged, paid take-home, AI pipeline edge |

## Plan

### Phase 1 — PDFs (sequential, ~3 min each)

- [ ] 1. Generate CV PDF for #022 VisCap Media — `python generate-pdf.py` (not .mjs — see fork notes above) with archetype framing per `reports/022-viscap-media-2026-04-26.md` Block E. Save to `output/`.
- [ ] 2. Generate CV PDF for #019 RemodelBoom
- [ ] 3. Generate CV PDF for #015 Kāsper
- [ ] 4. Generate CV PDF for #024 AJ Media
- [ ] 5. Generate CV PDF for #018 Odyssey
- [ ] 6. Generate CV PDF for #017 Publish Experts
- [ ] 7. Generate CV PDF for #027 GLP Winner

### Phase 2 — Apply (one at a time, operator reviews each before Submit)

- [ ] 8. **First apply: #015 Kāsper** (easiest — junior level, Canadian shop, normal form). Calibrate operator's preferences from his edits.
- [ ] 9. Apply to #022 VisCap Media (top pick). Connect to the named HM on LinkedIn before/after applying.
- [ ] 10. Apply to #019 RemodelBoom (with spec teardown attached if requested in form)
- [ ] 11. Apply to #024 AJ Media (with paid-trial pitch in cover letter)
- [ ] 12. Apply to #018 Odyssey (record Loom video — operator does this part)
- [ ] 13. Apply to #017 Publish Experts (paid-trial structure — clarify in cover letter)
- [ ] 14. Apply to #027 GLP Winner (portfolio + AI pipeline emphasis)

### Phase 3 — Tracker hygiene

- [ ] 15. After each apply: update `data/applications.md` status from `Evaluated` → `Applied` with date.
- [ ] 16. Update PDF emoji from ❌ to ✅ in tracker for each that got a PDF.
- [ ] 17. Set follow-up reminders: 7 days after each apply, run `/career-ops followup`.

## Process per application

1. operator says "apply to {company}"
2. Claude opens form via `/browser` (authenticated Chrome session)
3. Claude reads the form, identifies all required fields
4. Claude fills:
   - Identity (name, email, phone, location, LinkedIn) from `config/profile.yml`
   - Work auth: "Canadian citizen, no US visa needed for remote contractor work"
   - Salary expectation: from comp table per role type in `modes/_profile.md`
   - "Why this company / role" essays drafted from report Block E
   - Uploads CV PDF + cover letter
5. Claude STOPS before Submit. Shows operator the filled form.
6. operator reviews, edits anything, clicks Submit himself.
7. Claude updates tracker.

## Watchlist (no action today, monitor)

| Company | Why on watchlist | Re-check cadence |
|---------|------------------|------------------|
| Common Thread Collective | Top-target DTC growth shop. No creative role today. | Weekly |
| Tried & True Media | DR pedigree (Halbert/Schwartz lineage). Current openings closed. | Weekly |
| Darkroom | All current roles director+ level. Wait for IC opening. | Bi-weekly |
| HexClad | Heavy paid-social spend, will hire creative eventually. | Monthly |
| The Motley Fool | Geo blocker (US-only, 19 states). 18-36 month calibration target. Build spec investor advertorial. | Quarterly |

## What we are NOT doing in this phase

- Not auto-submitting any application — operator reviews each
- Not applying to scores 3.0-3.9 unless operator specifically requests
- Not applying to Motley Fool, whatskill.ai, Brightspeed, Common Thread Collective, etc. — these are watchlist or skip
- Not generating PDFs for sub-4.0 scores (run `/career-ops pdf {company}` later if needed)
- Not setting up automated /scan loops — operator can opt in separately

---

# Migration: wrap entire repo inside `_backend/`

**STATUS: ✅ COMPLETE (2026-05-01)** — All 5 phases executed. Ad-hoc follow-up: bridge `career-ops.mjs` was dropped in favor of `(cd _backend && X)` pattern + `Bash(cd _backend && *)` allowlist in `.claude/settings.json`. See parent `tasks/todo.md` for what's still pending in the workspace.

**Goal:** Clean up `F:\Projects\careers\` root so it can host a Karpathy-style wiki vault. Move the entire current career-ops repo (including `.git/`) into a `_backend/` subfolder. Add a thin wrapper at the parent so `/career-ops` still works.

**Final layout:**

```
F:\Projects\careers\
├── .claude\skills\career-ops\SKILL.md   # ~20-line wrapper
├── .obsidian\                           # stays at parent (vault config)
├── .gitignore                           # ignores _backend/
├── CLAUDE.md                            # parent — wiki conventions + 3-pointer backend section
├── career-ops.mjs                       # bridge script (~15 lines, sets cwd=_backend)
├── tasks\                               # NEW empty (frontend)
└── _backend\                            # everything currently at root
    ├── .git\                            # career-ops repo (upstream-tracked)
    ├── .claude\, .opencode\, .gemini\
    ├── modes\, templates\, batch\, dashboard\, fonts\, docs\, examples\
    ├── *.mjs scripts (15+), package.json, package-lock.json, node_modules\
    ├── cv.md, article-digest.md, portals.yml, config\, AGENTS.md, GEMINI.md, CLAUDE.md, README.md
    ├── data\, reports\, output\, interview-prep\, jds\, inbox\
    └── tasks\                           # current tasks/todo.md ends up here (backend ops)
```

**Decisions locked (confirmed in chat):**
- Hard wall: wiki = strategy/brain, backend = operational data/scripts. No symlinks across the wall.
- Two `.git` repos. Backend `.git` keeps upstream-tracked. Parent gets its own `.git` later (via wiki-builder bootstrap, separate task).
- Parent `.gitignore` lists `_backend/` to prevent double-tracking.
- Wrapper bridge = single `career-ops.mjs` at parent (option C). Backend scripts unchanged.
- Parent CLAUDE.md "Backend artifacts" section names exactly 3 paths: `_backend/cv.md`, `_backend/data/applications.md`, `_backend/reports/`. Everything else lives behind the inner skill on demand.
- Wiki-builder bootstrap is a SEPARATE follow-up task, not part of this migration.
- `tasks/` stays at parent (created fresh, empty). Current `tasks/todo.md` content moves with backend.
- `.obsidian/` stays at parent (it's the vault config; user said not to worry about it, will rediscover).

## Phase 0 — Pre-flight

- [ ] 1. Create filesystem backup at `F:\Projects\careers.backup\` (cp -r). This is the rollback lifeline.
- [ ] 2. Run `node update-system.mjs check`, `node doctor.mjs`, `node verify-pipeline.mjs` from current root. Capture green baselines.
- [ ] 3. Note current uncommitted state: `M AGENTS.md`, `M CONTRIBUTING.md`, `M examples/article-digest-example.md`, `M examples/cv-example.md`, `M examples/dual-track-engineer-instructor/cv.md`, `M tasks/todo.md`, plus untracked `batch/tracker-additions/merged/010..029` and `.obsidian/`. These move with everything; git sees them unchanged after move.

## Phase 1 — Move career-ops into `_backend/`

- [ ] 4. `mkdir F:\Projects\careers\_backend`
- [ ] 5. Move every file/folder at root into `_backend/` EXCEPT `.obsidian/` and `tasks/` (filesystem `mv`, not `git mv`, since `.git` itself moves).
   - Includes `.git`, `.github`, `.gitignore`, `.claude`, `.opencode`, `.gemini`, all `*.md` system docs, all `*.mjs` scripts, `modes/`, `templates/`, `batch/`, `dashboard/`, `docs/`, `fonts/`, `examples/`, `data/`, `reports/`, `output/`, `interview-prep/`, `jds/`, `inbox/`, `config/`, `cv.md`, `article-digest.md`, `portals.yml`, `package.json`, `package-lock.json`, `node_modules/`, `requirements.txt`, `VERSION`, `.update-dismissed`, `LICENSE`, `CITATION.cff`, `LEGAL_DISCLAIMER.md`.
- [ ] 6. Move `tasks/` into `_backend/` too (current todo.md content is backend operational work — fork mgmt + application phase). Then `mkdir F:\Projects\careers\tasks` for fresh empty frontend tasks/.
- [ ] 7. After moves, the parent root contains: `_backend/`, `.obsidian/`, `tasks/` (empty). Nothing else yet.

## Phase 2 — Verify backend still works

- [ ] 8. `git -C _backend status` — should show the same modified/untracked files as the pre-move baseline (paths unchanged from git's POV since the working tree moved with `.git`).
- [ ] 9. `node _backend/update-system.mjs check` — returns `dismissed` (uses `__dirname`, cwd-independent, confirmed earlier).
- [ ] 10. Run scripts that need cwd=_backend with explicit cd: `(cd _backend && node doctor.mjs)`, `(cd _backend && node verify-pipeline.mjs)`. Confirm green.
- [ ] 11. Sanity check on inner skill: `_backend/.claude/skills/career-ops/SKILL.md` is intact and unchanged.

## Phase 3 — Build the parent wrapper

- [ ] 12. Write `F:\Projects\careers\career-ops.mjs` (the bridge, ~15 lines per spec).
- [ ] 13. Write `F:\Projects\careers\.claude\skills\career-ops\SKILL.md`. Frontmatter: `name: career-ops`, `description`, `user_invocable: true`, `args: mode`, same `argument-hint` as inner. Body: instructs the agent to (a) Read `_backend/.claude/skills/career-ops/SKILL.md` and follow it exactly, (b) treat `_backend/` as the operational cwd for all scripts, (c) invoke scripts via `node career-ops.mjs <script.mjs> [args]` from parent OR `(cd _backend && node <script.mjs> [args])`.
- [ ] 14. Write `F:\Projects\careers\CLAUDE.md`. Sections:
   - One-liner: this is a wiki vault + career-ops backend
   - Backend artifacts (3 paths only): cv, tracker, reports
   - Invocation rule: `node career-ops.mjs <script>` or `(cd _backend && node <script>)`
   - Pointer: full career-ops context lives in `_backend/CLAUDE.md`, read it on `/career-ops` invocation
- [ ] 15. Write `F:\Projects\careers\.gitignore`. Lines: `_backend/`, `.obsidian/workspace.json`, `node_modules/`. Note: parent has no `.git` yet, so this file is dormant until wiki-builder bootstrap.

## Phase 4 — Verify integration

- [ ] 16. From a fresh agent invocation at parent root: confirm parent CLAUDE.md auto-loads, wrapper SKILL.md is discoverable.
- [ ] 17. Test bridge: `node career-ops.mjs update-system.mjs check` from parent — should match step 9's output.
- [ ] 18. Test bridge with args: `node career-ops.mjs verify-pipeline.mjs` — same as step 10.
- [ ] 19. Trigger `/career-ops` (no args) → wrapper loads, delegates to inner skill, inner skill shows discovery menu.
- [ ] 20. Trigger `/career-ops tracker` → wrapper delegates, inner skill reads `_backend/data/applications.md`, returns overview.
- [ ] 21. NOT testing: PDF generation, scan, full pipeline. Those need real input. Spot-test happens in normal use after migration.

## Phase 5 — Cleanup

- [ ] 22. Keep `F:\Projects\careers.backup\` for at least one full week of normal use before deletion. Not now.
- [ ] 23. The migration is COMPLETE. Wiki-builder bootstrap is a separate task (not part of this).

## Rollback plan

If anything is broken after migration and unfixable in <30 min:

```
rm -rf F:/Projects/careers
mv F:/Projects/careers.backup F:/Projects/careers
```

Backup is the only safety net since `.git` moves into `_backend/`. Do NOT delete `careers.backup/` until the new layout has been used in anger.

## Out of scope for this migration

- Wiki-builder bootstrap (`wiki/`, `sources/`, `_index.yaml`, parent `.git`) — separate task
- Any change to inner career-ops files (modes, scripts, configs) — keeping backend pristine for upstream
- Any change to how career-ops outputs reports (still goes to `_backend/reports/`) — option (a) hard wall
- GitHub remote for the eventual wiki repo — handled later
- Permission allowlist hygiene for `Bash(node career-ops.mjs *)` — runs once via `/fewer-permission-prompts` after migration if useful
