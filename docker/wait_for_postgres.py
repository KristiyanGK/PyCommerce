#!/usr/bin/env python
"""Wait until Postgres accepts connections, then exit."""

import os
import sys
import time

import psycopg


def main() -> int:
    host = os.environ.get("POSTGRES_HOST")
    if not host:
        return 0

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
            return 0
        except Exception as exc:
            print(f"waiting for postgres ({attempt}/{attempts}): {exc}", flush=True)
            time.sleep(2)

    print("postgres did not become ready in time", flush=True)
    return 1


if __name__ == "__main__":
    sys.exit(main())
