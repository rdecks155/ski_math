# ski_math/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import CustomUser, Student
from .forms import TeacherSignUpForm, StudentSignUpForm
from .decorators import student_required, teacher_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)


class SignUp(generic.CreateView):
    form_class = TeacherSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class studentSignUp(generic.CreateView):
    form_class = StudentSignUpForm
    success_url = reverse_lazy('studentsignup')
    template_name = 'signup.html'

class GameView(TemplateView):
    template_name = 'gamelayout.html'

class Stats(TemplateView):
    template_name = 'stats.html'

class TeacherStats(TemplateView):
    model = Student
    context_object_name = 'student'
    template_name = 'teacherstats.html'

    def get(self, request):
        student_list = CustomUser.objects.filter(is_student__exact=True)
        context = {'student_list': student_list}
        return render(request, 'teacherstats.html', context)
        