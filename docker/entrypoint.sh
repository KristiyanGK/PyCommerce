#!/bin/sh
# Container startup: wait until Postgres accepts connections, apply migrations,
# collect static files for WhiteNoise, then exec the image CMD (Gunicorn).
set -eu

python - <<'PY'
import os
import sys
import time

import psycopg

host = os.environ.get("POSTGRES_HOST")
if not host:
    raise SystemExit(0)

conninfo = {
    "host": host,
    "port": os.environ.get("POSTGRES_PORT", "5432"),
    "dbname": os.environ.get("POSTGRES_DB", "pycommerce"),
    "user": os.environ.get("POSTGRES_USER", "pycommerce"),
    "password": os.environ.get("POSTGRES_PASSWORD", ""),
}

attempts = 30
for attempt in range(1, attempts + 1):
    try:
        with psycopg.connect(**conninfo, connect_timeout=3) as conn:
            conn.execute("SELECT 1")
        print(f"postgres is ready ({host})", flush=True)
        raise SystemExit(0)
    except Exception as exc:
        print(f"waiting for postgres ({attempt}/{attempts}): {exc}", flush=True)
        time.sleep(2)

print("postgres did not become ready in time", flush=True)
raise SystemExit(1)
PY

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
