#!/bin/bash

echo "Dealing with migrations..."
python -m poetry run python manage.py makemigrations --no-input
python -m poetry run python manage.py migrate --no-input

echo "Collecting static files..."
python -m poetry run python manage.py collectstatic --no-input

echo "Starting server..."
python -m poetry run python manage.py runserver