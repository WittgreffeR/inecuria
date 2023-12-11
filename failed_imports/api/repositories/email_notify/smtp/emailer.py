from typing import Any, Iterable

from django.core import mail

from config.settings import DEFAULT_FROM_EMAIL


def send_notify_email(addresses: Iterable[str], message: dict[str, Any]) -> None:
    mail.send_mail(
        subject="Failed Imports Service Report | TDi Digital",
        message=message["plain"],
        html_message=message["html"],
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[address for address in addresses],
        fail_silently=False,
    )
