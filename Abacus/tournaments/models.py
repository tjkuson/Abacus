from datetime import date

from django.db import models
from django.urls import reverse


class Tournament(models.Model):
    name = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text=f"The full name (for example, ‘Manchester Open {date.today().year}’)",
        verbose_name="name",
    )
    slug = models.SlugField(
        max_length=16,
        blank=False,
        null=False,
        help_text=f"The end part of the URL (for example, ‘mancopen{date.today().year}’)",
        verbose_name="URL slug",
    )
    is_active = models.BooleanField(
        # TODO: Does this need a help_text?
        default=True,
        blank=False,
        null=False,
        verbose_name="is active",
    )

    def get_absolute_url(self) -> str:
        return reverse("tournament_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return str(self.name)
