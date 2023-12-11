from typing import Optional

from failed_imports.api import models, values

from .values import PROVISIONS_TABLE, STANDARDS_TABLE, DataType


def model_to_failed_import(input: models.FailedImport) -> values.FailedImport:
    return values.FailedImport(
        id=input.data_id,
        name=input.name,
        data_type=input.data_type,
        reason=input.reason,
        updated_at=input.updated_at,
        url=data_type_lookup(input.data_type, input.airtable_id),
    )


def data_type_lookup(
    data_type: str, airtable_record: Optional[str] = None
) -> Optional[str]:
    if data_type == DataType.STANDARD.value:
        return _construct_url(STANDARDS_TABLE, airtable_record)

    if data_type == DataType.PROVISION.value:
        return _construct_url(PROVISIONS_TABLE, airtable_record)

    return None


def _construct_url(table: str, airtable_record: Optional[str]) -> str:
    result = f"https://airtable.com/{table}"

    if airtable_record:
        result += f"/{airtable_record}"

    return result
