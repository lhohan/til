# Deployment Context

This document provides essential context for understanding and modifying the TIL site deployment pipeline. For implementation details, read the source code directly (`.github/workflows/deploy.yml`, `justfile`, `.work-dir/site/prepare-site.py`).

## Overview

The deployment pipeline automatically builds and deploys the TIL site to a Hetzner instance when commits are pushed to the `main` branch. The same `just` commands work locally and in GitHub Actions for consistency.

**Note**: User provisioning (creating the dedicated ployment user, SSH keys, directory permissions) is handled in a separate repository via Ansible. This document assumes that setup is complete.

## Deployment User & Infrastructure

- **User**: dedicated user (created via Ansible provisioning)
- **Group**: `deployer` (for consistent permissions with existing Ansible setup)
- **Host**: IP Address of Hetzner instance)
- **Deployment Path**: `/srv/www/til.hanlho.com/public/`

## GitHub Secrets

Configure these secrets in your GitHub repository settings (`https://github.com/lhohan/til/settings/secrets/actions`):

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `HETZNER_SSH_KEY` | Private SSH key for deployment | Contents of `~/.ssh/<til private key>` |
| `HETZNER_HOST` | Hetzner server IP address | e.g. `46.62.228.207` |
| `HETZNER_USER` | Deployment username | name of dedicated user |

## Environment Variables

The deployment pipeline uses these environment variables (required, no defaults):

| Variable | Description | 
|----------|-------------|
| `HETZNER_HOST` | Hetzner server IP | 
| `HETZNER_USER` | SSH username | 
| `HETZNER_SSH_KEY_PATH` | Path to SSH private key | 
| `DEPLOY_PATH` | Remote deployment directory | 
| `HEALTH_CHECK_URL` | Site URL for health check | 

For local deployment setup a `.env` with these variables.

## Deployment Commands

The GitHub Action and local deployment use the same `just` commands for consistency:

```bash
# Full deployment (build + ssh check + deploy + health check)
just deploy
```

## GitHub Action Workflow

The workflow (`.github/workflows/deploy.yml`) runs on every push to `main`:

1. Checks out the repository
2. Sets up Nix environment
3. Loads environment variables from GitHub Secrets
4. Runs the same `just` commands as local deployment
5. Includes health check verification

## Local Testing

Before pushing to `main`, test the deployment locally:

```bash
just deploy
```

**Benefits**: Same commands run locally and in CI, so you can verify changes before committing.

## Key Implementation Files

- `.github/workflows/deploy.yml` — GitHub Action workflow
- `justfile` — Deployment commands and build orchestration

## Troubleshooting

### SSH Connection Issues
```bash
# Test SSH manually
just check-ssh
```

### Missing Environment Variables
```bash
# Verify .env file exists and is populated
cat .env

# Check GitHub Secrets are configured
# https://github.com/lhohan/til/settings/secrets/actions
```

## Security Model

The dedicated user is isolated with minimal permissions:
- ✅ Can write only to `/srv/www/til.hanlho.com/public/`
- ❌ Cannot access other sites' directories
- ❌ Cannot reload Caddy or modify system configuration
- ❌ Cannot escalate privileges

If the SSH key is compromised, an attacker can only modify TIL site content, not other infrastructure.
