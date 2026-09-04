# Hallcy Da'at — Public Learning Sandbox

The public face of the Hallcy ecosystem. A gamified AI learning arcade where players and AI solve logic puzzles side by side.

> 🛡️ **Security-first public surface.** This repo contains ZERO proprietary code, ZERO API keys, ZERO companion art, and ZERO private Hallcy infrastructure. Everything real lives in private repos.

## What you'll find here
- ⌨️ **Monkeytype Alpha Matrix** — type code blocks, race the AI
- 🌱 **8-Bit Watering Garden** — solve memory puzzles to grow plants
- 🐞 **Pattern Debug Hunter** — spot syntax bugs in real time
- 💼 **Brand Sponsorship Portal** — verified socials required
- 📝 **Beta Feedback Terminal** — rate, suggest, report bugs (local log only)

## Run it
```bash
python -m venv .venv && source .venv/bin/activate
pip install streamlit google-genai
export GEMINI_API_KEY=your_key_here   # optional — runs in sandbox mode without it
streamlit run app.py
```

## Security
See [SECURITY.md](SECURITY.md). Dependency audit: clean. No secrets in git history. Feedback never leaves your machine. Vendored upstream trees (Prisma, PhotoGIMP) have been removed — they do not belong inside this sandbox.

## License
All Rights Reserved. See [ANTI_SPINOFF.md](ANTI_SPINOFF.md).
