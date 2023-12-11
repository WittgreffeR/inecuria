from typing import Iterable

from failed_imports.api.values import FailedImport

from ..service import EmailNotifyService
from .backend import create_notify_message
from .emailer import send_notify_email
from .serialisers import addresses_to_list


class SmtpEmailNotifyService(EmailNotifyService):
    def email_failures(
        self, addresses: str, failed_imports: Iterable[FailedImport], days: int
    ) -> None:
        send_notify_email(
            addresses_to_list(addresses), create_notify_message(failed_imports, days)
        )
