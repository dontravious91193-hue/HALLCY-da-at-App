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

## Hardening checklist (enable in repo Settings → Code security)
1. **Dependabot alerts** — on (free for public repos)
2. **Secret scanning** — on
3. **Push protection** — on (blocks secret pushes before they land)
4. **Code scanning** (CodeQL) — on
5. **Dependency review** on PRs — on

## Verified clean (automated audit)
- 0 known vulnerable dependencies (`@google/genai`, `dotenv`, `express`, `typescript`, `vite`)
- 0 code-scanning alerts
- 0 security advisories
- No hardcoded secrets detected in tracked files
- `.gitignore` excludes `.env`, `node_modules/`, `dist/`, `daat_feedback.jsonl`

## Reporting a vulnerability
Open a private advisory via **Security → Advisories → Report a vulnerability**, or email the maintainer. Do not file a public issue for security findings.
