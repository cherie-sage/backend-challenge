"""
Minimal Django settings for the live-coding challenge environment.

This is intentionally bare-bones: just enough to run Django + DRF against
Postgres with token auth already wired up.

The database connection is driven entirely by environment variables, which the
development container is expected to supply. See README.md.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key-not-for-production")

# Fine for a local, throwaway development environment. Do not deploy as-is.
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Django rejects a form POST when the browser's Origin header doesn't match the
# address Django thinks it is serving. That happens constantly in development
# because a proxy sits in front: Codespaces terminates TLS at its edge, and
# VS Code's port forwarding presents the app as localhost. Both routes have to
# be listed, or every form POST fails with "Origin checking failed".
CSRF_TRUSTED_ORIGINS = [
    # Codespaces public forwarded port
    "https://*.app.github.dev",
    "https://*.github.dev",
    # VS Code port forwarding, and plain local use
    "http://localhost:8000",
    "https://localhost:8000",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "challenge"),
        "USER": os.environ.get("POSTGRES_USER", "challenge"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "challenge"),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = []  # not relevant for a short-lived interview environment

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
