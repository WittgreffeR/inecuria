from django.urls import path

from failed_imports.health_check import views

app_name = "health_check"


urlpatterns = [
    path("", views.index, name="index"),
]
