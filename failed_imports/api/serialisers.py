from typing import Any, cast

from rest_framework import serializers
from rest_framework.request import Request

from failed_imports.api.values import FailedImport


class FailedImportRequestSerialiser(serializers.Serializer):  # type:ignore[type-arg]
    id = serializers.CharField()
    name = serializers.CharField()
    data_type = serializers.CharField()
    reason = serializers.CharField(required=False, default=None)
    airtable_id = serializers.CharField(required=False, default=None)


def request_to_failed_import(request: Request) -> FailedImport:
    return _data_to_failed_import(_request_to_data(request))


def _data_to_failed_import(data: dict[str, Any]) -> FailedImport:
    return FailedImport(**data)


def _request_to_data(request: Request) -> dict[str, Any]:
    serialised = FailedImportRequestSerialiser(data=request.data)
    serialised.is_valid(raise_exception=True)
    return cast(dict[str, Any], serialised.validated_data)
