from games.models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    home_team_name = serializers.CharField(source='home_team.name', read_only=True)
    home_team_image = serializers.CharField(source='home_team.image', read_only=True)
    away_team_name = serializers.CharField(source='away_team.name', read_only=True)
    away_team_image = serializers.CharField(source='away_team.image', read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'home_team', 'away_team', 'start_date', 'start_time', 'home_team_name', 'home_team_image',
                  'away_team_name', 'away_team_image')


