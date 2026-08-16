#!/bin/sh
# Container startup: wait until Postgres accepts connections, apply migrations,
# collect static files for WhiteNoise, then exec the image CMD (Gunicorn).
set -eu

SCRIPT_DIR=$(dirname "$0")
python "$SCRIPT_DIR/wait_for_postgres.py"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
