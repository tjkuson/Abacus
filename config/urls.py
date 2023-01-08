# django-stubs can't handle appending to a list of URLResolvers:
# https://github.com/typeddjango/django-stubs/issues/550
# type: ignore

from django.conf import settings
from django.contrib import admin
from django.urls import URLResolver, include, path
from django.views import defaults as default_views

urlpatterns: list[URLResolver] = [
    path("admin/", admin.site.urls),
    path("", include("Abacus.pages.urls")),
    path("", include("Abacus.tournaments.urls")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit these
    # urls in the browser to see how these error pages look like.
    urlpatterns = [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        *urlpatterns,
    ]
