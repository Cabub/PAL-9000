#!/bin/bash

# Get the absolute path of the current directory
DIR="$(pwd)"

rm -f "$DIR/target/function.zip"

python -m venv .venv

# Activate the virtual environment
source "$DIR/.venv/bin/activate"

# Install any necessary dependencies
pip install -r "$DIR/requirements.txt"

# Package the Lambda function code and the virtual environment's dependencies into a zip file
cd "$DIR/.venv/lib/python3.9/site-packages/"
zip -r9 "/tmp/function.zip" .
cd "$DIR/src"
zip -g /tmp/function.zip *.py

# Move function.zip to ./target
mv /tmp/function.zip "$DIR/target/"
