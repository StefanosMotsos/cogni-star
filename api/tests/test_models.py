from django.test import TestCase

from api.models import Planet


class PlanetModelTest(TestCase):
    def setUp(self):
        self.planet = Planet.objects.create(name="Tatooine", terrain="dessert", population="200000")

    def test_str_returns_name(self):
        result = str(self.planet)

        self.assertEqual(result, "Tatooine")

