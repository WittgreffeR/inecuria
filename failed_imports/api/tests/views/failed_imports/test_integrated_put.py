from http import HTTPStatus

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from failed_imports.api import models

pytestmark = pytest.mark.integrated


@pytest.mark.django_db
def test_put_http_status() -> None:
    """
    Given a request to PUT a failed imports entry
    It returns HTTP status 200 (ok)
    """
    input_data = {
        "id": "test_id",
        "name": "test_name",
        "data_type": "test_type",
        "reason": "test_reason",
        "airtable_id": "test_airtable_id",
    }

    response = APIClient().put(path=reverse("api:failedimport"), data=input_data)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_bad_request_http_status() -> None:
    """
    Given a bad request to PUT a failed imports entry
    It returns HTTP status 400 (bad request)
    """
    input_data = {"bogus": "nonsense"}

    response = APIClient().put(path=reverse("api:failedimport"), data=input_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.django_db
def test_create_model() -> None:
    """
    Given a (correctly formatted) failed imports request
    It correctly creates a failed imports model
    """
    input_data = {
        "id": "test_id",
        "name": "test_name",
        "data_type": "test_type",
        "reason": "test_reason",
        "airtable_id": "test_airtable_id",
    }

    APIClient().put(path=reverse("api:failedimport"), data=input_data)

    created_model = models.FailedImport.objects.get(data_id=input_data["id"])

    assert created_model.data_id == input_data["id"]
    assert created_model.name == input_data["name"]
    assert created_model.data_type == input_data["data_type"]
    assert created_model.reason == input_data["reason"]


@pytest.mark.django_db
def test_no_duplicate_imports() -> None:
    """
    Given a failed import request that is identical to another failed import already in the system
    It does not duplicate it and instead updates the updated_at time
    """
    input_data = {
        "id": "test_id",
        "name": "test_name",
        "data_type": "test_type",
        "reason": "test_reason",
        "airtable_id": "test_airtable_id",
    }

    APIClient().put(path=reverse("api:failedimport"), data=input_data)

    first_updated_at = models.FailedImport.objects.get(
        data_id=input_data["id"]
    ).updated_at

    APIClient().put(path=reverse("api:failedimport"), data=input_data)

    assert models.FailedImport.objects.all().count() == 1
    assert (
        models.FailedImport.objects.get(data_id=input_data["id"]).updated_at
        > first_updated_at
    )
