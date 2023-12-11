from datetime import datetime, timedelta

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from config.containers import container


def landing_page(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "site/index.html",
        {
            "failed_imports": container.failed_imports_repo.get_all_failed_imports(
                earliest=datetime.now() - timedelta(days=7)
            )
        },
    )
