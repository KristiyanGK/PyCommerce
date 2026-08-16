import os
from pathlib import Path

from .env import env_bool, env_list
from .storage import build_storages, minio_enabled

# src/ — parent of the pycommerce package
BASE_DIR = Path(__file__).resolve().parents[2]

DEBUG = env_bool("DJANGO_DEBUG", default=True)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = (
            "django-insecure-y*n=p3!i1*69rxqaw&8!i+(@=1igb^@j6@jm$md2xyjww&oyqi"
        )
    else:
        raise ValueError("DJANGO_SECRET_KEY must be set when DJANGO_DEBUG is false")

ALLOWED_HOSTS = env_list(
    "DJANGO_ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1", "[::1]"] if DEBUG else [],
)
CSRF_TRUSTED_ORIGINS = env_list("DJANGO_CSRF_TRUSTED_ORIGINS")
SERVE_MEDIA = env_bool("DJANGO_SERVE_MEDIA", default=DEBUG)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "storages",
    "product_manager.apps.ProductManagerConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pycommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pycommerce.wsgi.application"


def _databases() -> dict:
    if host := os.environ.get("POSTGRES_HOST"):
        return {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": os.environ.get("POSTGRES_DB", "pycommerce"),
                "USER": os.environ.get("POSTGRES_USER", "pycommerce"),
                "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
                "HOST": host,
                "PORT": os.environ.get("POSTGRES_PORT", "5432"),
            }
        }
    return {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


DATABASES = _databases()

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

USE_MINIO = minio_enabled()
STORAGES = build_storages(debug=DEBUG)

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "PyCommerce API",
    "DESCRIPTION": "Product and category operations for the e-commerce service.",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    },
}
