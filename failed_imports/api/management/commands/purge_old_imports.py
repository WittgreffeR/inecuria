from typing import Any

from django.core.management.base import BaseCommand

from config.containers import container


class Command(BaseCommand):
    help = "Deletes all failed imports older than the specified number of days. Setting the number of days to 0 will delete all stored failed imports."

    def add_arguments(self, parser) -> None:  # type: ignore
        parser.add_argument("days", type=int)

    def handle(self, *args: list[Any], **options: Any) -> None:
        container.failed_imports_repo.purge_old_imports(days_limit=options["days"])
