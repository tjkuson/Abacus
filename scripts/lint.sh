#!/bin/bash

echo "Checking with isort..."
python -m poetry run isort . --check --profile black

echo "Checking with black..."
python -m poetry run black . --check

echo "Checking with DjLint..."
python -m poetry run djlint . --lint

echo "Checking with mypy..."
python -m poetry run mypy . --strict