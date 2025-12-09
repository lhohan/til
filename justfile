set shell := ["bash", "-c"]
set dotenv-load := true  # Load .env file automatically for all recipes

# Main build task - prepares site and updates README
build-content: _prepare-site _update-readme

dev: build-content
    cd .work-dir/site && zola serve --drafts

build: build-content zola-build pagefind

zola-build:
    cd .work-dir/site && zola build

pagefind:
    cd .work-dir/site && pagefind --site public

check:
    cd .work-dir/site && zola check

new-til topic slug:
    python3 .work-dir/scripts/new_til.py {{topic}} {{slug}}

# Hidden tasks (prefixed with _ to hide from just --list)
_prepare-site:
    python3 .work-dir/site/prepare-site.py

_update-readme:
    python3 .work-dir/scripts/update-readme.py

clean:
    rm -rf .work-dir/site/public/

# Deployment commands (for local testing)
# These mirror the GitHub Action steps for local development

check-ssh:
    # Configure SSH for deployment (idempotent)
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh

    # Validate required environment variables
    if [ -z "${HETZNER_HOST}" ]; then echo "Error: HETZNER_HOST environment variable is required"; exit 1; fi
    if [ -z "${HETZNER_USER}" ]; then echo "Error: HETZNER_USER environment variable is required"; exit 1; fi
    if [ -z "${HETZNER_SSH_KEY_PATH}" ]; then echo "Error: HETZNER_SSH_KEY_PATH environment variable is required"; exit 1; fi

    # Ensure SSH key exists and has correct permissions
    if [ ! -f "${HETZNER_SSH_KEY_PATH}" ]; then echo "Error: SSH key not found at ${HETZNER_SSH_KEY_PATH}"; exit 1; fi
    chmod 600 "${HETZNER_SSH_KEY_PATH}"

    # Add host to known_hosts (idempotent - only add if not already present)
    if ! grep -q "${HETZNER_HOST}" ~/.ssh/known_hosts 2>/dev/null; then ssh-keyscan "${HETZNER_HOST}" >> ~/.ssh/known_hosts; fi

    # Test SSH connection
    ssh -i ${HETZNER_SSH_KEY_PATH} "${HETZNER_USER}"@"${HETZNER_HOST}" echo "SSH connection successful"

deploy-sync:
    # Deploy using rsync
    # Validate required environment variables
    if [ -z "${HETZNER_HOST}" ]; then echo "Error: HETZNER_HOST environment variable is required"; exit 1; fi
    if [ -z "${HETZNER_USER}" ]; then echo "Error: HETZNER_USER environment variable is required"; exit 1; fi
    if [ -z "${HETZNER_SSH_KEY_PATH}" ]; then echo "Error: HETZNER_SSH_KEY_PATH environment variable is required"; exit 1; fi
    if [ -z "${DEPLOY_PATH}" ]; then echo "Error: DEPLOY_PATH environment variable is required"; exit 1; fi

    rsync -avz --delete --chmod=u+rwX,g+rX,o+rX \
        -e "ssh -i $HETZNER_SSH_KEY_PATH" \
        .work-dir/site/public/ \
        ${HETZNER_USER}@${HETZNER_HOST}:${DEPLOY_PATH}

deploy-health-check:
    if [ -z "${HEALTH_CHECK_URL}" ]; then echo "Error: HEALTH_CHECK_URL environment variable is required"; exit 1; fi
    response=$(curl -s -o /dev/null -w "%{http_code}" "${HEALTH_CHECK_URL}")
    if [ "$response" -ne 200 ]; then echo "Health check failed: HTTP $response"; exit 1; fi
    echo "Health check passed: Site is accessible"

# Main deployment command (runs all steps)
deploy:
    just build
    just check-ssh
    just deploy-sync
    just deploy-health-check
