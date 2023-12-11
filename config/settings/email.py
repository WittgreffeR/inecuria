from .dotenv import env

EMAIL_USE_TLS = True

EMAIL_HOST = env.str("EMAIL_HOST", default=None)
EMAIL_PORT = env.int("EMAIL_PORT", default=25)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="failed-imports")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default=None)
SERVER_EMAIL = env.str("SERVER_EMAIL", default="no-reply@tdi-digital.com")
DEFAULT_FROM_EMAIL = env.str("EMAIL_DEFAULT_FROM", default=SERVER_EMAIL)


if not EMAIL_HOST:
    raise ValueError("EMAIL_HOST not configured")

if not EMAIL_HOST_PASSWORD:
    raise ValueError("EMAIL_HOST_PASSWORD not configured")
