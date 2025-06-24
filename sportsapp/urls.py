from django.urls import path
from .views import sportslist,teamlist,playerslist,matchlist

urlpatterns =[
    path('sports/',sportslist.as_view(),name='sports-list'),
    path('team/',teamlist.as_view(),name="team-list"),
    path('players/',playerslist.as_view(),name="players-list"),
    path('matches/',matchlist.as_view(),name='match-list')
]