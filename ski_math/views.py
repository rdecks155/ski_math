# ski_math/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Game(TemplateView):
    template_name = 'game.html'

class Stats(TemplateView):
    template_name = 'stats.html'
