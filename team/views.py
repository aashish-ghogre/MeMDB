from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from team.models import Team
from team.serializers import TeamSerializer


class TeamList(generics.ListCreateAPIView):
    """"
    API End point to Create Team
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


