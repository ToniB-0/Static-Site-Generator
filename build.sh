#!/bin/bash
set -e
echo "Building site for GitHub Pages..."
cd "$(dirname "$0")"
python3 src/main.py /"Static-Site-Generator/"
echo "Production build complete (output in ./docs)"

