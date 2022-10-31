#!/bin/bash

echo "Apply database migrations"

while ! python manage.py migrate 2>&1; do
   echo "Migration is in progress status"
   sleep 3
done
  echo "Django docker is fully configured successfully."

exec "$@"