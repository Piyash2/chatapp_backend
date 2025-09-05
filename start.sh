#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
python manage.py migrate --run-syncdb

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "Starting application..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120 --access-logfile - --error-logfile -
