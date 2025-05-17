#!/usr/bin/env bash

# Safely removes Crawlect virtual environment and optional build artifacts.

set -e

echo "Tearing down Crawlect virtual environment..."

# Handle flags
FORCE=false
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -f|--force) FORCE=true ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
    shift
done

# Confirm deletion if not forced
confirm() {
    read -p "Are you sure you want to delete the virtual environment and cleanup files? [y/N] " answer
    case "$answer" in
        [Yy]* ) ;;
        * ) echo "Aborted."; exit 0 ;;
    esac
}

# Check if venv exists
if [ -d "venv" ]; then
    echo "Found ./venv directory."

    # Ask before deletion unless forced
    if [ "$FORCE" = false ]; then
        confirm
    fi

    # Deactivate venv if active
    if [ "$VIRTUAL_ENV" ]; then
        echo "Deactivating active virtual environment..."
        deactivate 2>/dev/null || echo "(No need to deactivate)"
    fi

    # Remove venv directory
    echo "Removing ./venv..."
    rm -rf venv || { echo "Failed to remove ./venv"; exit 1; }

    # Optional cleanup: __pycache__ and .pyc
    echo "Cleaning up __pycache__ and .pyc files..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
    find . -type f -name "*.pyc" -delete 2>/dev/null

    echo "Environment cleaned up!"
else
    echo "No venv directory found. Nothing to remove."
fi