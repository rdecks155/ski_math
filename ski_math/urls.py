# ski_math/urls.py
from django.urls import path

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('game/', views.Game.as_view(), name='game'),
    path('stats/', views.Stats.as_view(), name='stats'),
]