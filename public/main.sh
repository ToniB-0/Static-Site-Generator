#!/bin/bash
set -e  # Stop if any command fails

echo "Building site..."

# Always run from the project root (so paths are correct)
cd "$(dirname "$0")"

# Remove any existing 'public' directory if it exists
if [ -d "public" ]; then
    echo "Removing old public directory..."
    rm -rf public
fi

# Run the Python build process
python3 src/main.py

echo "Site build complete. Starting server at http://localhost:8888"

# Start a simple web server from the public directory
cd public
python3 -m http.server 8888

