from typing import Iterable, Protocol

from failed_imports.api.values import FailedImport


class EmailNotifyService(Protocol):
    def email_failures(
        self, addresses: str, failed_imports: Iterable[FailedImport], days: int
    ) -> None:
        ...
