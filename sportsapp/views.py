from rest_framework import generics
from .models import SportsTournament,team,players,matches
from .serializers import sportsserializer,teamserializer,playersserializer,matchesserializer

class sportslist(generics.ListCreateAPIView):
    queryset=SportsTournament.objects.all()
    serializer_class=sportsserializer

class teamlist(generics.ListCreateAPIView):
    queryset=team.objects.all()
    serializer_class=teamserializer

class playerslist(generics.ListCreateAPIView):
    queryset=players.objects.all()
    serializer_class=playersserializer

class matchlist(generics.ListCreateAPIView):
    queryset=matches.objects.all()
    serializer_class=matchesserializer