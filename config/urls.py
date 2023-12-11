from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check/", include("inecuria.health_check.urls")),
    path("api/", include("inecuria.api.urls")),
    path("", include("inecuria.site.urls")),
]
