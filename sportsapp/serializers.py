from rest_framework import serializers
from .models import SportsTournament
from .models import team,players,matches
from django.contrib.auth.models import User

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

class userserializer(serializers.ModelSerializer):
    password =serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email']

        def create(self,validate_data):
            user= User.objects.create(username=validate_data['username'],password=validate_data['password'],email=validate_data.get('email',''))
            return user
            