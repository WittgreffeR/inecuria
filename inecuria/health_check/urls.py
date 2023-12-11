from django.urls import path

from inecuria.health_check import views

app_name = "health_check"


urlpatterns = [
    path("", views.index, name="index"),
]
