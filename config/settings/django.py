import pathlib
from typing import Final

from .dotenv import env
from .paths import BASE_DIR

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "webpack_loader",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "failed_imports.api",
    "failed_imports.core",
    "failed_imports.site",
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

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["failed_imports/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "string_if_invalid": "<< MISSING VARIABLE %s >>" if DEBUG else "",
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Cookies
SESSION_COOKIE_DOMAIN = (
    ".tdi-digital.com" if not env.str("DEBUG", False) else "localhost"
)
SESSION_COOKIE_HTTPS = True if not env.str("DEBUG", False) else False
SESSION_COOKIE_SAMESITE: Final = "Lax"

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = str(pathlib.Path(BASE_DIR, "static"))
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static_build",
]

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "STATS_FILE": str(pathlib.Path(BASE_DIR, "static/webpack-stats.json")),
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

if env.bool("USE_DEFAULT_STATICFILES_STORAGE", default=False):
    # Use the default staticfiles storage for tests to avoid running collectstatic.
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
else:
    STATICFILES_STORAGE = "whitenoise.storage.StaticFilesStorage"

# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES
WHITENOISE_KEEP_ONLY_HASHED_FILES = True
# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_SKIP_COMPRESS_EXTENSIONS
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = (
    "jpg",
    "jpeg",
    "png",
    "gif",
    "webp",
    "zip",
    "gz",
    "tgz",
    "bz2",
    "tbz",
    "xz",
    "br",
    "swf",
    "flv",
    "woff",
    "woff2",
    "mp4",
)


# Force HTTPS
if env.bool("FORCE_HTTPS", default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = [
    "https://*.127.0.0.1",
    "https://*.tdi-digital.com",
]  # allow all because this is an API as well as a Site and could be called from a non-browser
