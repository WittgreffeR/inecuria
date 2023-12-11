from django.urls import include, path

from inecuria.api import views

app_name = "api"

inecuria_api_urls = [
    path(
        "",
        include(
            [
                path(
                    "",
                    views.RootView.as_view(),
                    name="root",
                ),
            ],
        ),
    ),
]

urlpatterns = [*inecuria_api_urls]
