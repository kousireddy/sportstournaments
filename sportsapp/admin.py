from django.contrib import admin
from .models import SportsTournament,team,players,matches

# Register your models here.

admin .site.register(SportsTournament)
admin.site.register(team)
admin.site.register(players)
admin.site.register(matches)
