from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    class Meta:
        db_table = 'Team'

