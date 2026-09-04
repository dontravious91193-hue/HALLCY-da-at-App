# Hallcy Da'at — Public Security Posture

This repo is the **only public** surface of the Hallcy ecosystem. Everything proprietary — the Hive Engine, Sim kernel, companion art, private bridges — lives in private repos. This sandbox must never leak them.

## What is public here
- Gamified learning arcade (Monkeytype Alpha Matrix, 8-Bit Watering Garden, Pattern Debug Hunter)
- Beta feedback terminal (local JSONL log, nothing exfiltrated)
- Brand sponsorship portal (form only, no backend storage of PII beyond what you choose to share)
- Loading-screen art and cinematic opening manifest

## What is NOT here (and must never be committed)
- Gemini / Google API keys → env var `GEMINI_API_KEY` only
- Any private Hallcy repo URLs, tokens, or credentials
- Companion art sheets, Live2D models, or rigging specs
- Sim kernel, agent brains, or production configs
- Real player PII — feedback is anonymized by design
- Vendored upstream projects (Prisma, PhotoGIMP, autoremesher) — these belong in their own repos, not inside this sandbox

## Incident response (leaked secret found)
1. **Revoke first** — Google Cloud Console → APIs & Services → Credentials; MongoDB Atlas → Database Access. Deleting the file does not stop an attacker who already copied it.
2. **Remove from history** — `git filter-repo --path public/prisma --invert-paths`, then force-push. Only needed if crawlers may have cached old commits.
3. **Mark alerts resolved** — Security → Secret scanning → mark each alert Revoked.
4. **Enable push protection** — Settings → Code security → push protection on. Blocks the next leak before it lands.

## Hardening checklist (enable in repo Settings → Code security)
1. **Dependabot alerts** — on (free for public repos)
2. **Secret scanning** — on
3. **Push protection** — on (blocks secret pushes before they land)
4. **Code scanning** (CodeQL) — on
5. **Dependency review** on PRs — on

## Verified clean (automated audit)
- Vendored `public/prisma/` and `public/PhotoGIMP/` trees removed from the working tree
- `.gitignore` now blocks those trees, `.env*`, and the feedback log
- `app.py` reads `GEMINI_API_KEY` from env only — no hardcoded key
- Feedback writes to a local file that is gitignored

## Reporting a vulnerability
Open a private advisory via **Security → Advisories → Report a vulnerability**, or email the maintainer. Do not file a public issue for security findings.
