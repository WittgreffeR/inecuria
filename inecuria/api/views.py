from http import HTTPStatus

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class RootView(APIView):
    VIEW_NAME = "root"

    def get(self, request: Request) -> Response:
        return Response(
            status=HTTPStatus.OK,
            data={"hello": "world"},
            headers={"Version": str(request.version)},
        )
