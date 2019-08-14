from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from games.models import Game
from games.serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """"
    API End point to view or edit Games
    """
    queryset = Game.objects.select_related('home_team','away_team')
    serializer_class = GameSerializer


class GameDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.select_related('home_team','away_team')
    serializer_class = GameSerializer


