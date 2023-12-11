import pytest
from django.core import mail

from failed_imports.api.repositories.failed_imports.django.tests.factories import (
    FailedImportFactory,
)

from ..email_failures import email_failures

pytestmark = pytest.mark.integrated


@pytest.mark.django_db
def test_email_failures_entire_process() -> None:
    """
    Given a set of failed imports in the database, and a set of comma-separated email addresses
    It composes and sends an email
    """
    FailedImportFactory.create()

    email_failures(
        days=1,
        addresses="testemail@tdi-sustainability.com, thomas.esting@tdi-sustainability.com, t.est@tdi-sustainability.com",
    )

    assert len(mail.outbox) == 1
