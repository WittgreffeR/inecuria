from django.urls import include, path

from failed_imports.api import views

app_name = "api"

failed_imports_api_urls = [
    path(
        "",
        include(
            [
                path(
                    "",
                    views.RootView.as_view(),
                    name="root",
                ),
                path(
                    "import/",
                    views.FailedImportView.as_view(),
                    name=views.FailedImportView.VIEW_NAME,
                ),
            ],
        ),
    ),
]

urlpatterns = [*failed_imports_api_urls]
