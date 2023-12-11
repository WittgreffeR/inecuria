from typing import Any, Iterable

from django.template.loader import render_to_string

from config.settings import FAILED_IMPORTS_HOST
from failed_imports.api.values import FailedImport

from .serialisers import messages_to_dict


def create_notify_message(
    failed_imports: Iterable[FailedImport], days: int
) -> dict[str, Any]:
    if _check_for_failed_imports(failed_imports):
        return messages_to_dict(html=_assemble_html_message(failed_imports, days))

    return messages_to_dict(
        plain=f"No assets have failed to import within the last {_use_correct_grammar(days)}."
    )


def _check_for_failed_imports(failed_imports: Iterable[FailedImport]) -> bool:
    return len([fimport for fimport in failed_imports]) > 0


def _assemble_html_message(failed_imports: Iterable[FailedImport], days: int) -> str:
    return render_to_string(
        "email/table.html",
        {
            "failed_imports": failed_imports,
            "correct_grammar": _use_correct_grammar(days),
            "fis_website": FAILED_IMPORTS_HOST,
        },
    )


def _use_correct_grammar(days: int) -> str:
    if days == 1:
        return "day"

    return f"{days} days"
