from .env import env_bool, env_str


def minio_enabled() -> bool:
    return env_bool("DJANGO_USE_MINIO") or bool(env_str("MINIO_ENDPOINT"))


def build_storages(*, debug: bool) -> dict:
    storages = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": (
                "django.contrib.staticfiles.storage.StaticFilesStorage"
                if debug
                else "whitenoise.storage.CompressedManifestStaticFilesStorage"
            ),
        },
    }
    if minio_enabled():
        storages["default"] = {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": _minio_options(),
        }
    return storages


def _minio_options() -> dict:
    bucket = env_str("MINIO_BUCKET", "pycommerce")
    endpoint = env_str("MINIO_ENDPOINT")
    access_key = env_str("MINIO_ACCESS_KEY")
    secret_key = env_str("MINIO_SECRET_KEY")
    if not endpoint or not access_key or not secret_key:
        raise ValueError(
            "MINIO_ENDPOINT, MINIO_ACCESS_KEY, and MINIO_SECRET_KEY must be set "
            "when MinIO storage is enabled"
        )

    return {
        "access_key": access_key,
        "secret_key": secret_key,
        "bucket_name": bucket,
        "endpoint_url": endpoint,
        "region_name": env_str("MINIO_REGION", "us-east-1"),
        "addressing_style": "path",
        "custom_domain": env_str(
            "MINIO_CUSTOM_DOMAIN",
            f"localhost:9000/{bucket}",
        ),
        "url_protocol": env_str("MINIO_URL_PROTOCOL", "http:"),
        "use_ssl": endpoint.startswith("https"),
        "querystring_auth": False,
        "default_acl": None,
        "signature_version": "s3v4",
    }
