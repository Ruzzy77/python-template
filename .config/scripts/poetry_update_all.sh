#!/bin/bash
# Shell Script to update all poetry projects

# Update installed packages
poetry update

# Update lock file
# poetry update --lock

# Install dependencies from lock file
poetry install --no-root --sync

# Remove unneeded dependencies
poetry lock

# Clean the cache
# poetry cache clear . --all --no-interaction
