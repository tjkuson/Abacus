from django.urls import path

from .views import LicenceView

urlpatterns = [
    path("licence/", LicenceView.as_view(), name="licence"),
]
