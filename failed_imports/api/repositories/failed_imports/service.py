from datetime import datetime
from typing import Iterable, Optional, Protocol

from failed_imports.api import values


class FailedImportsRepository(Protocol):
    def create_failed_import(
        self, FailedImport: values.FailedImport
    ) -> values.FailedImport:
        ...

    def get_all_failed_imports(
        self,
        earliest: Optional[datetime] = None,
        latest: Optional[datetime] = None,
    ) -> Iterable[values.FailedImport]:
        ...

    def purge_old_imports(self, days_limit: int) -> None:
        ...
