from datetime import datetime, timedelta

from config.containers import container


def email_failures(days: int, addresses: str) -> None:
    container.email_service.email_failures(
        addresses,
        container.failed_imports_repo.get_all_failed_imports(
            earliest=datetime.now() - timedelta(days)
        ),
        days,
    )
