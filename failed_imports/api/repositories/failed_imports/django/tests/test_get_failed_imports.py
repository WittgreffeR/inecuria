from datetime import datetime

import pytest

from config.containers import container

from .factories import FailedImportFactory

pytestmark = pytest.mark.isolated


@pytest.mark.django_db
def test_get_all_failed_imports() -> None:
    """
    Given a database of failed imports and no filters for updated_at
    It returns all the failed imports, sorted by the latest updated_at time
    """
    failed_import_old = FailedImportFactory.create(
        data_id="old_id", updated_at=datetime.now()
    )
    failed_import_new = FailedImportFactory.create(
        data_id="new_id", updated_at=datetime.now()
    )
    all_imports = container.failed_imports_repo.get_all_failed_imports()

    results = [fimport.id for fimport in all_imports]

    assert results[0] == failed_import_new.data_id
    assert results[1] == failed_import_old.data_id


@pytest.mark.django_db
def test_filter_imports_earliest() -> None:
    """
    Given a database of failed imports and ONLY the earliest filter
    It returns only the failed imports that fall within the filters
    """
    # The failed imports must be set up like this and cannot have manually set updated_at datetimes
    # Because updated_at is automatically updated when saved and will override manual datetimes
    FailedImportFactory.create()
    test_earliest = datetime.now()
    FailedImportFactory.create()
    FailedImportFactory.create()
    FailedImportFactory.create()

    filtered_imports = container.failed_imports_repo.get_all_failed_imports(
        earliest=test_earliest
    )
    results = [fimport.id for fimport in filtered_imports]

    assert len(results) == 3


@pytest.mark.django_db
def test_filter_imports_latest() -> None:
    """
    Given a database of failed imports and ONLY the latest filter
    It returns only the failed imports that fall within the filters
    """
    # The failed imports must be set up like this and cannot have manually set updated_at datetimes
    # Because updated_at is automatically updated when saved and will override manual datetimes
    FailedImportFactory.create()
    FailedImportFactory.create()
    FailedImportFactory.create()
    test_latest = datetime.now()
    FailedImportFactory.create()

    filtered_imports = container.failed_imports_repo.get_all_failed_imports(
        latest=test_latest
    )
    results = [fimport.id for fimport in filtered_imports]

    assert len(results) == 3


@pytest.mark.django_db
def test_filter_imports_earliest_to_latest() -> None:
    """
    Given a database of failed imports and BOTH the earliest and latest filters
    It returns only the failed imports that fall within the filters
    """
    # The failed imports must be set up like this and cannot have manually set updated_at datetimes
    # Because updated_at is automatically updated when saved and will override manual datetimes
    FailedImportFactory.create()
    test_earliest = datetime.now()
    FailedImportFactory.create()
    FailedImportFactory.create()
    test_latest = datetime.now()
    FailedImportFactory.create()

    filtered_imports = container.failed_imports_repo.get_all_failed_imports(
        test_earliest, test_latest
    )
    results = [fimport.id for fimport in filtered_imports]

    assert len(results) == 2
