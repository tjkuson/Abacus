#!/bin/bash

echo "Formatting with isort..."
python -m poetry run isort . --profile black

echo "Formatting with black..."
python -m poetry run black .

echo "Formatting with DjLint..."
python -m poetry run djlint .