from datetime import datetime
from typing import Iterable, Optional

from failed_imports.api import models, values


def create_failed_import(input: values.FailedImport) -> models.FailedImport:
    failed_import = _get_or_create_failed_import(input)

    failed_import.airtable_id = _resolve_airtable_id(
        failed_import.airtable_id, input.airtable_id
    )

    failed_import.save()

    return failed_import


def _get_or_create_failed_import(input: values.FailedImport) -> models.FailedImport:
    asset, created = models.FailedImport.objects.get_or_create(
        data_id=input.id,
        reason=input.reason,
        defaults={
            "name": input.name,
            "data_type": input.data_type,
            "airtable_id": input.airtable_id,
        },
    )

    return asset


def _resolve_airtable_id(
    model_airtable_id: Optional[str], value_airtable_id: Optional[str]
) -> Optional[str]:
    if value_airtable_id and not model_airtable_id:
        return value_airtable_id

    return None


def retrieve_failed_imports(
    earliest: Optional[datetime] = None, latest: Optional[datetime] = None
) -> Iterable[models.FailedImport]:
    all_imports = models.FailedImport.objects.all()

    if earliest:
        all_imports = all_imports.filter(updated_at__gte=earliest)

    if latest:
        all_imports = all_imports.filter(updated_at__lte=latest)

    return all_imports.order_by("-updated_at")
