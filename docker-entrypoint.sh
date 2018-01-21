#!/bin/bash

while [[ $(python3 "wait_for_mysql.py") != "true" ]]; do
  echo "Couldn't connect, sleeping..."
  sleep 1
done

# Update database migrations
echo "Update database migrations"
python3 manage.py makemigrations survey

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Load fixtures
echo "Load fixtures"
python3 manage.py loaddata survey/fixtures/superuser.json

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
