#!/usr/bin/env bash

# setup.sh – Initializes Crawlect virtual environment and installs dependencies.

echo "Setting up Crawlect virtual environment..."

# Detect platform (Git Bash / Unix-like)
case "$(uname -s)" in
    Linux*|Darwin*)
        ACTIVATE="source venv/bin/activate"
        ;;
    MINGW*|MSYS*|CYGWIN*)
        ACTIVATE="source venv/Scripts/activate"
        ;;
    *)
        echo "Unsupported platform: $(uname -s)"
        exit 1
        ;;
esac

# Step 1: Create venv
echo "Creating virtual environment in ./venv"
if python -m venv venv 2>/dev/null; then
    echo "Created venv using 'python'"
elif py -m venv venv 2>/dev/null; then
    echo "Created venv using 'py'"
else
    echo "Failed to create venv"; exit 1
fi

# Step 2: Activate venv
echo "Activating virtual environment"
eval "$ACTIVATE" || { echo "Failed to activate venv"; exit 1; }

# Step 3: Install requirements
echo "Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

echo "Crawlect is ready! You can now run: python -m crawlect.crawlect"