from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from team.models import Team
import unittest


# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.team_id = "1"
        self.team_name = "India"
        self.team_image = "India.png"
        self.team = Team(name=self.team_name, image=self.team_image)

    def test_model_can_create_a_team(self):
        """Test the game model can create a game."""
        old_count = Team.objects.count()
        self.team.save()
        new_count = Team.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            "name": "India",
            "image":"India.png"
        }
        self.response = self.client.post(
            reverse('team'),
            self.team_data,
            format="json")

    def test_api_can_create_team(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


if __name__ == '__main__':
    unittest.main()
