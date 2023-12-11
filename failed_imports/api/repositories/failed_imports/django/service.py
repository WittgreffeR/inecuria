from datetime import datetime, timedelta
from typing import Iterable, Optional

from failed_imports.api import values

from ..service import FailedImportsRepository
from . import backend
from .serialisers import model_to_failed_import


class DjangoFailedImportsRepository(FailedImportsRepository):
    def create_failed_import(
        self, FailedImport: values.FailedImport
    ) -> values.FailedImport:
        return model_to_failed_import(backend.create_failed_import(FailedImport))

    def get_all_failed_imports(
        self,
        earliest: Optional[datetime] = None,
        latest: Optional[datetime] = None,
    ) -> Iterable[values.FailedImport]:
        return [
            model_to_failed_import(fi)
            for fi in backend.retrieve_failed_imports(earliest, latest)
        ]

    def purge_old_imports(self, days_limit: int) -> None:
        for failed_import in backend.retrieve_failed_imports(
            latest=datetime.now() - timedelta(days_limit)
        ):
            failed_import.delete()
