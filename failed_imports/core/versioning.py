from typing import Any

from rest_framework.request import Request
from rest_framework.versioning import BaseVersioning

from config import settings


class AcceptVersionHeaderVersioning(BaseVersioning):
    def determine_version(
        self, request: Request, *args: list[Any], **kwargs: dict[str, Any]
    ) -> str:
        return request.META.get("HTTP_ACCEPT_VERSION", settings.DEFAULT_API_VERSION)
