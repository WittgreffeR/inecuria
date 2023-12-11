from http import HTTPStatus

import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.integrated


def test_returns_OK() -> None:
    url = reverse("health_check:index")

    response = Client().get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == "👌"
