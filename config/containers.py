from failed_imports.api.repositories.email_notify import (
    EmailNotifyService,
    SmtpEmailNotifyService,
)
from failed_imports.api.repositories.failed_imports import (
    DjangoFailedImportsRepository,
    FailedImportsRepository,
)


class DependencyContainer:
    _failed_imports_repo: FailedImportsRepository
    _email_service: EmailNotifyService

    def __init__(self) -> None:
        self._failed_imports_repo = DjangoFailedImportsRepository()
        self._email_service = SmtpEmailNotifyService()

    @property
    def failed_imports_repo(self) -> FailedImportsRepository:
        return self._failed_imports_repo

    @failed_imports_repo.setter
    def failed_imports_repo(self, repo: FailedImportsRepository) -> None:
        self._failed_imports_repo = repo

    @property
    def email_service(self) -> EmailNotifyService:
        return self._email_service

    @email_service.setter
    def email_service(self, service: EmailNotifyService) -> None:
        self._email_service = service


container = DependencyContainer()
