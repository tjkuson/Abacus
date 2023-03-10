from django.contrib import admin

from .models import Tournament


class TournamentAdmin(admin.ModelAdmin[Tournament]):
    model = Tournament
    list_display = ["name", "is_active"]


admin.site.register(Tournament, TournamentAdmin)
