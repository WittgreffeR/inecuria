import pytest

from ..backend import create_notify_message
from .factories import FailedImportFactory

pytestmark = pytest.mark.integrated


def test_assemble_message() -> None:
    """
    Given a set of failed imports from within a given number of days (2)
    It returns a correctly assembled email message listing the failed imports
    """
    failed_imports = [FailedImportFactory.create(), FailedImportFactory.create()]

    message = create_notify_message(failed_imports, 2)

    assert message["html"] is not None


def test_assemble_message_if_empty() -> None:
    """
    Given a number of days (2) with no failed imports that occurred in the given time period
    It returns a correctly assembled email message saying there were no failures
    """
    message = create_notify_message([], 2)

    assert message["plain"] == "No assets have failed to import within the last 2 days."
    assert message["html"] is None
