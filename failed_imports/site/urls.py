from django.urls import path

from failed_imports.site import views

app_name = "site"

site_urls = [
    path("", views.landing_page, name="landing-page"),
]

urlpatterns = [*site_urls]
