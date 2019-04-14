# ski_math/urls.py
from django.urls import path

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('game/', views.GameView.as_view(), name='game'),
    path('stats/', views.Stats.as_view(), name='stats'),
    path('studentsignup/', views.studentSignUp.as_view(), name='studentsignup'),
    path('teacherstats', views.TeacherStats.as_view(), name='teacherstats'),
    path('game/playerhistory/', views.PlayerHistory, name='playerhistory'),
    path('game/ski_math/writeplayer', views.WriteHistory, name='writeplayer'),
    path('certificate/', views.Certificate, name='certificate')
]