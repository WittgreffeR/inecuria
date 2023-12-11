from .dotenv import env

FAILED_IMPORTS_HOST = env.str("FAILED_IMPORTS_HOST", default="failed-imports")
