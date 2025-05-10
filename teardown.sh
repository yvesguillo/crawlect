#!/usr/bin/env bash

# teardown.sh – Removes Crawlect virtual environment safely

echo "Tearing down Crawlect virtual environment..."

# Check if venv exists
if [ -d "venv" ]; then
    echo "Deactivating and removing ./venv..."

    # Try to deactivate if currently active
    if [ "$VIRTUAL_ENV" ]; then
        deactivate 2>/dev/null || echo "(No need to deactivate)"
    fi

    # Remove the venv directory
    rm -rf venv || {
        echo "Failed to remove ./venv"
        exit 1
    }

    echo "Environment cleaned up!"
else
    echo "No venv directory found. Nothing to remove."
fi