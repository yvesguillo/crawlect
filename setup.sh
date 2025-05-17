#!/usr/bin/env bash

# Initializes Crawlect virtual environment and installs dependencies.

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

# Detect Python command with working venv support
echo "Detecting Python interpreter with venv support..."

detect_python() {
    for cmd in python3 python py; do
        if command -v $cmd &>/dev/null; then
            version=$($cmd --version 2>&1)
            echo "Found $cmd ($version)"
            if $cmd -m venv --help &>/dev/null; then
                PYTHON_CMD=$cmd
                return 0
            else
                echo "  ↳ But: $cmd does not support venv"
            fi
        fi
    done
    return 1
}

if detect_python; then
    echo "Using Python command: $PYTHON_CMD"
else
    if [[ "$OSTYPE" == "linux-gnu"* ]] && command -v apt &>/dev/null; then
        echo "Python was found, but the 'venv' module is missing."
        echo "Attempting to install 'python3-venv' using apt..."
        read -p "Do you want to proceed? [Y/n] " yn
        case $yn in
            [Yy]* | "" )
                sudo apt update && sudo apt install -y python3-venv
                echo "Rechecking Python after install..."
                if detect_python; then
                    echo "Using Python command: $PYTHON_CMD"
                else
                    echo "Still no Python interpreter with venv support. Aborting."
                    exit 1
                fi
                ;;
            * )
                echo "Cannot continue without 'venv'. Aborting."
                exit 1
                ;;
        esac
    else
        echo "No compatible Python interpreter with venv support found."
        exit 1
    fi
fi

# Step 1: Create venv
echo "Creating virtual environment in ./venv"
if $PYTHON_CMD -m venv venv 2>/dev/null; then
    echo "Created venv using '$PYTHON_CMD'"
else
    echo "Failed to create venv with $PYTHON_CMD"
    exit 1
fi

# Step 2: Activate venv
echo "Activating virtual environment"
eval "$ACTIVATE" || { echo "Failed to activate venv"; exit 1; }

# Step 3: Install requirements with fallback
pip_install_with_fallback() {
    CMD=$1
    shift
    echo "Running: $CMD $*"
    $CMD "$@" && return
    $PYTHON_CMD -m $CMD "$@" && return
    echo "Failed to $CMD $*" >&2
    exit 1
}

echo "Installing dependencies"
pip_install_with_fallback pip install --upgrade pip
pip_install_with_fallback pip install -r requirements.txt

echo "Crawlect is ready! You can now run: \"$PYTHON_CMD -m crawlect\"."