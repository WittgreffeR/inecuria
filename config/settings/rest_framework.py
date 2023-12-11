from .dotenv import env

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_VERSIONING_CLASS": "failed_imports.core.versioning.AcceptVersionHeaderVersioning",
}

ENABLE_REST_FRAMEWORK_PERMISSIONS = env.bool(
    "ENABLE_REST_FRAMEWORK_PERMISSIONS", default=True
)
if ENABLE_REST_FRAMEWORK_PERMISSIONS:
    REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ]
else:
    REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
        "rest_framework.permissions.AllowAny",
    ]
