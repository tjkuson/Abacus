from django.forms import ModelForm

from .models import Tournament


class TournamentCreateForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ("name", "slug", "is_active")


class TournamentUpdateForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ("name", "slug", "is_active")
