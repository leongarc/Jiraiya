from rest_framework import serialzers
from .models import Team

class TeamSerializer(serialzers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'team_name', 'player_count', 'coach_name', 'goals_scored')