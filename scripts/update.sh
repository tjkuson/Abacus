#!/bin/bash

echo "Update Python dependencies..."
python -m poetry update

echo "Update npm..."
npm update