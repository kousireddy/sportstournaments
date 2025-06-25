from django.urls import path
from .views import sportslist,teamlist,playerslist,matchlist,sportsdetail,teamdetail,playersdetail,matchdetail,UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns =[

    path('register/',UserCreate.as_view,name='create-user'),
    path ('token/',TokenObtainPairView.as_view(),name='get-token'),
    path('refresh/',TokenRefreshView.as_View(),name='refresh'),
    path('sports/',sportslist.as_view(),name='sports-list'),
    path('team/',teamlist.as_view(),name="team-list"),
    path('players/',playerslist.as_view(),name="players-list"),
    path('matches/',matchlist.as_view(),name='match-list'),
    path('sportsdetail/<int:pk>',sportsdetail.as_view(),name='sports-deatil'),
    path('teamdetail/<int:pk>',teamdetail.as_view(),name='team-detail'),
    path('playerdetail/<int:pk>',playersdetail.as_view(),name='player-detail'),
    path('matchdetail/<int:pk>',matchdetail.as_view(),name='math-detail'),

]