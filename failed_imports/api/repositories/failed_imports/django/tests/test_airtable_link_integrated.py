import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from config.containers import container

pytestmark = pytest.mark.integrated


@pytest.mark.django_db
def test_update_airtable_link() -> None:
    """
    Given a failed import with no airtable_id
    Updating it with an airtable_id adds the id and constructs a specific record link
    """
    input_1 = {
        "id": "2.4.30.14",
        "name": "Publicly disclose payments to governments.",
        "data_type": "Provision",
        "reason": "Fake failure for testing purposes",
    }

    APIClient().put(path=reverse("api:failedimport"), data=input_1)

    input_2 = {
        "id": "2.4.30.14",
        "name": "Publicly disclose payments to governments.",
        "data_type": "Provision",
        "reason": "Fake failure for testing purposes",
        "airtable_id": "rectLmY2KEKHMTnrV",
    }

    APIClient().put(path=reverse("api:failedimport"), data=input_2)

    updated_imports = container.failed_imports_repo.get_all_failed_imports()
    results = [fimport for fimport in updated_imports]

    assert (
        results[0].url
        == "https://airtable.com/appjDXUPkfYwb65DU/tbl7KmA5iAq28i1a1/viwHwGauUCVGxveMQ/rectLmY2KEKHMTnrV"
    )
