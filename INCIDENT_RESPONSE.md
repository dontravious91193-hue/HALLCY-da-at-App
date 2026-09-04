# Incident response runbook — leaked secret

If GitHub secret scanning flags a credential in any Hallcy repo:

1. **Revoke immediately** at the provider (Google Cloud Console, MongoDB Atlas, GitHub, etc.). File deletion does not stop an attacker who already copied it.
2. **Remove from the working tree** — delete the file, update `.gitignore`.
3. **Scrub history** if the repo was public:
   ```bash
   pip install git-filter-repo
   git clone --mirror https://github.com/dontravious91193-hue/REPO.git
   cd REPO.git
   git filter-repo --path path/to/leaked/file --invert-paths
   git push --force --all
   ```
4. **Mark the alert Revoked** in Security → Secret scanning.
5. **Enable push protection** in Settings → Code security so the next leak is blocked before it lands.

Never commit `.env`, real API keys, or vendored upstream test trees. Secrets live in env vars or a secret manager — never in git.
