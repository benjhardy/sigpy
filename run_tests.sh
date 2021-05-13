#!/bin/bash
set -e
rm -rf docs/generated/
coverage run -m unittest
flake8
sphinx-build -W docs docs/_build/html
