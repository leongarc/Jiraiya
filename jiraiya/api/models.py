from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=15, unique=True)
    player_count = models.IntegerField(default=0)
    coach_name = models.CharField(max_length=25, default="none")
    goals_scored = models.IntegerField(default=0)
