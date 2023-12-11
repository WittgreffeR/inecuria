from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check/", include("failed_imports.health_check.urls")),
    path("api/failed-imports/", include("failed_imports.api.urls")),
    path("", include("failed_imports.site.urls")),
]
