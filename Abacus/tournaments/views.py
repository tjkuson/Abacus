from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import TournamentCreateForm, TournamentUpdateForm
from .models import Tournament


def get_tournament_from_slug(tournament_slug: str):
    """Return tournament from given tournament slug; else, return 404."""

    try:
        # Store tournament using slug captured in URL.
        return Tournament.objects.get(slug=tournament_slug)
    except Tournament.DoesNotExist as exc:
        raise Http404 from exc
    except Tournament.MultipleObjectsReturned as exc:
        msg = "More than one tournament has the same slug."
        raise RuntimeWarning(msg) from exc


class TournamentListView(ListView):
    model = Tournament
    template_name = "tournament/tournaments_list.html"


class TournamentCreateView(CreateView):
    model = Tournament
    form_class = TournamentCreateForm
    success_url = reverse_lazy("tournaments_list")
    template_name = "tournaments/tournament_create.html"


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = "tournaments/tournament_detail.html"


class TournamentUpdateView(UpdateView):
    model = Tournament
    form_class = TournamentUpdateForm
    template_name = "tournaments/tournament_update.html"
