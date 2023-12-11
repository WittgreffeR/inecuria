from http import HTTPStatus

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from config.containers import container
from inecuria.api.serialisers import request_to_failed_import


class RootView(APIView):
    VIEW_NAME = "root"

    def get(self, request: Request) -> Response:
        return Response(
            status=HTTPStatus.OK,
            data={"hello": "world"},
            headers={"Version": str(request.version)},
        )


class FailedImportView(APIView):
    VIEW_NAME = "failedimport"

    def put(self, request: Request) -> Response:
        container.failed_imports_repo.create_failed_import(
            request_to_failed_import(request)
        )
        return Response(status=HTTPStatus.OK)
