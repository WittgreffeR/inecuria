import pytest
from freezegun import freeze_time

from failed_imports.api import models

from ..service import DjangoFailedImportsRepository
from .factories import FailedImportFactory

pytestmark = pytest.mark.isolated


@pytest.mark.django_db
def test_purge_imports() -> None:
    """
    Given a failed import that is older than the specified time limit
    It deletes ONLY the failed import that is outside the limit, and none within it
    """
    with freeze_time("2000-01-01 12:00:00"):
        FailedImportFactory.create()
    FailedImportFactory.create()

    DjangoFailedImportsRepository().purge_old_imports(days_limit=7)

    assert models.FailedImport.objects.all().count() == 1
