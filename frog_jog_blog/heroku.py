"""
Special settings that will only be used when deploying to Heroku
"""
from os import path, environ
import dj_database_url
from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + path.join(BASE_DIR, "../db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    path.join(BASE_DIR, "static"),
]
SECRET_KEY = environ.get("django_key")
ALLOWED_HOSTS = ["*"]

MIDDLEWARE = (
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE,
)
