from django.urls import path

from .views import (
    TournamentCreateView,
    TournamentDetailView,
    TournamentListView,
    TournamentUpdateView,
)

urlpatterns = [
    path("", TournamentListView.as_view(), name="tournament_list"),
    path(
        "tournaments/create/", TournamentCreateView.as_view(), name="tournament_create"
    ),
    path("<slug:slug>/", TournamentDetailView.as_view(), name="tournament_detail"),
    path(
        "<slug:slug>/update/", TournamentUpdateView.as_view(), name="tournament_update"
    ),
]
