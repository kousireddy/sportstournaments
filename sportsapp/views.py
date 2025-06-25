from rest_framework import generics
from .models import SportsTournament,team,players,matches
from .serializers import sportsserializer,teamserializer,playersserializer,matchesserializer,userserializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class sportslist(generics.ListCreateAPIView):
    queryset=SportsTournament.objects.all()
    serializer_class=sportsserializer
    permission_class=[IsAuthenticated]

class teamlist(generics.ListCreateAPIView):
    queryset=team.objects.all()
    serializer_class=teamserializer
    permission_class=[IsAuthenticated]

class playerslist(generics.ListCreateAPIView):
    queryset=players.objects.all()
    serializer_class=playersserializer
    permission_class=[IsAuthenticated]

class matchlist(generics.ListCreateAPIView):
    queryset=matches.objects.all()
    serializer_class=matchesserializer
    permission_class=[IsAuthenticated]

class sportsdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportsTournament.objects.all()
    serializer_class = sportsserializer
    permission_class=[IsAuthenticated]

class teamdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=team.objects.all()
    serializer_class=teamserializer
    permission_class=[IsAuthenticated]

class playersdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=team.objects.all()
    serializer_class=playersserializer
    permission_class=[IsAuthenticated]

class matchdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=matches.objects.all()
    serializer_class=matchesserializer
    permission_class=[IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=userserializer
    permission_class=[]