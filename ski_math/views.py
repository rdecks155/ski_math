# ski_math/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import CustomUser
from .forms import TeacherSignUpForm, StudentSignUpForm
from .decorators import student_required, teacher_required

class SignUp(generic.CreateView):
    form_class = TeacherSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class studentSignUp(generic.CreateView):
    form_class = StudentSignUpForm
    success_url = reverse_lazy('studentsignup')
    template_name = 'signup.html'

class Game(TemplateView):
    template_name = 'gamelayout.html'

class Stats(TemplateView):
    template_name = 'stats.html'
