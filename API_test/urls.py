from django.urls import path
from .views import gamesListView, gamesListView2

urlpatterns = [
  path('games/', gamesListView.as_view(), name='game_list'),
  path('games/<int:id>/', gamesListView.as_view(), name='game'),
  path('games/name/<str:name>/', gamesListView2.as_view(), name='game_id') 
]
