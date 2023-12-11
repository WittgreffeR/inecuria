from typing import Any

from django.core.management.base import BaseCommand

from ..service.email_failures import email_failures


class Command(BaseCommand):
    help = "Sends a list of all failed imports that occurred in the last given number of days to the given list of email addresses. Addresses must be contained in one string, separated by commas."

    def add_arguments(self, parser) -> None:  # type: ignore
        parser.add_argument("days", type=int)
        parser.add_argument("addresses", type=str)

    def handle(self, *args: list[Any], **options: Any) -> None:
        email_failures(options["days"], options["addresses"])
