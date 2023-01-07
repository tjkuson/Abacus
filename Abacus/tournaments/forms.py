from django.forms import ModelForm

from .models import Tournament


class TournamentCreateForm(ModelForm[Tournament]):
    class Meta:
        model = Tournament
        fields = ("name", "slug", "is_active")


class TournamentUpdateForm(ModelForm[Tournament]):
    class Meta:
        model = Tournament
        fields = ("name", "slug", "is_active")
