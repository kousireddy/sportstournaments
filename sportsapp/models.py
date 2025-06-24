from django.db import models

# Create your models here.
class  SportsTournament(models.Model):
    tournamentID = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    sport =models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    
    def __str__(self):
        return self.name
    
class team(models.Model):
    name=models.CharField(max_length=255)
    couch=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class players(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    position=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class matches(models.Model):
    name=models.CharField(max_length=255)
    matchdate =models.DateField()
    location =models.CharField(max_length=255)

    def __str__(self):
        return self.name


