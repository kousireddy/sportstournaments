from rest_framework import serializers
from .models import SportsTournament
from .models import team,players,matches

class sportsserializer(serializers.ModelSerializer):
    class Meta:
        model = SportsTournament
        fields ='__all__'
class teamserializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = '__all__'
class playersserializer(serializers.ModelSerializer):
    class Meta:
        model =players
        fields='__all__'
class matchesserializer(serializers.ModelSerializer):
    class Meta:
        model=matches
        fields='__all__'
