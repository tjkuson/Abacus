from django.test import TestCase

from .models import Tournament


class TournamentTests(TestCase):
    """Test tournament model."""

    def test_create_tournament(self) -> None:
        """Test a tournament can be created."""

        tournament = Tournament.objects.create(name="Example IV", slug="example")
        self.assertEqual(tournament.name, "Example IV")
        self.assertEqual(tournament.slug, "example")
        self.assertTrue(tournament.is_active)
        self.assertEqual(str(tournament), "Example IV")
        self.assertEqual(tournament.get_absolute_url(), "/example/")
