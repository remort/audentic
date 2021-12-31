#!/bin/sh

set -e

wait-for-it \
  --service ${DB_HOST}:${DB_PORT} \
  -- echo "Postgres is up"

echo 'Run main app'
alembic upgrade head
exec python run.py
