from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from games.models import Game
import unittest


# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.game_id = "1"
        self.game_home_team = "1"
        self.game_away_team = "2"
        self.game_start_date = "2019-05-16"
        self.game_start_time = "2019-05-16T08:24:00"
        self.gameList = Game(home_team=self.game_home_team, away_team=self.game_away_team,
                             start_date=self.game_start_date, start_time=self.game_start_time)

    def test_model_can_create_a_game(self):
        """Test the game model can create a game."""
        old_count = Game.objects.count()
        self.gameList.save()
        new_count = Game.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.game_data = {
            "home_team": 301,
            "away_team": 302,
            "start_date": "2019-05-15",
            "start_time": "2019-05-15T07:43:00Z"
        }
        self.response = self.client.post(
            reverse('game-list'),
            self.game_data,
            format="json")

    def test_api_can_create_game(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


if __name__ == '__main__':
    unittest.main()
