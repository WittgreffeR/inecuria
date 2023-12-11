from http import HTTPStatus
from typing import Optional

from rest_framework.response import Response


def api_error_response(
    api_version: str, status_code: HTTPStatus, message: Optional[str] = None
) -> Response:
    return Response(
        status=status_code,
        headers={"Version": api_version},
        data={"error": message} if message else None,
    )
