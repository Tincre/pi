#!/bin/bash
echo "Locking dependencies using Python $(python --version)."

echo "Generating requirements.txt..."
pipenv requirements --hash > requirements.txt
echo "Now generating dev-requirements.txt..."
pipenv requirements --dev --hash > dev-requirements.txt
echo "All dependencies generated with hashes. You should probably commit the changes."
echo "You may do so via the following command:"
echo "ga && gc ':heavy_plus_sign: <dependencyName> added'"
