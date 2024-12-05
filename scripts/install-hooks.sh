#!/bin/bash

# This script installs the pre-commit hook into the .git/hooks/ directory

# Check if the pre-commit hook already exists
if [ -f .git/hooks/pre-commit ]; then
    echo "Pre-commit hook already exists. Please remove it before reinstalling."
    exit 1
fi

# Create a symbolic link for the pre-commit hook
ln -s ../../scripts/pre-commit .git/hooks/pre-commit

# Make sure the pre-commit hook is executable
chmod +x .git/hooks/pre-commit

echo "Pre-commit hook installed successfully."

