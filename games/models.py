from django.db import models
from team.models import Team

# Create your models here.
class Game(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Game_Home_Team', db_column='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Game_Away_Team', db_column='away_team')
    start_date = models.DateField()
    start_time = models.DateTimeField()

    class Meta:
        db_table = 'Game'

