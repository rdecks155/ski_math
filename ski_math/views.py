# ski_math/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .models import CustomUser, Student
from .forms import TeacherSignUpForm, StudentSignUpForm
from .decorators import student_required, teacher_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.core import serializers 
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import parse_qs

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

    def get(self, request):
        current_user = request.user
        account_info = Student.objects.filter(user_id__exact=current_user.id)
        context = {'account_info': account_info}
        return render(request, 'stats.html', context)

class TeacherStats(TemplateView):
    model = Student
    context_object_name = 'student'
    template_name = 'teacherstats.html'

    def get(self, request):
        student_data = Student.objects.all()
        print("student data: ", student_data)
        context = {'student_list': student_data}
        print("context", context)
        return render(request, 'teacherstats.html', context)

def PlayerHistory(request):
    current_user = request.user
    student = Student.objects.filter(user_id__exact=current_user.id).values()
    student_list = list(student)
    return JsonResponse(student_list, safe=False)

@csrf_exempt
def WriteHistory(request):
    if request.method == 'POST':
        current_user = request.user
        data = parse_qs(request.body.decode("utf-8"))
        # print("Data: ", data)
        Student.objects.filter(user_id__exact=current_user.id).update(highestScore = data['highestScore'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(addHighestScore = data['addHighestScore'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(subHighestScore = data['subHighestScore'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(recHighestScore = data['recHighestScore'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(addLevel = data['addLevel'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(subLevel = data['subLevel'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(recLevel = data['recLevel'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(highestLevel = data['highestLevel'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(levelHighestScore = data['levelHighestScore'][0])
        Student.objects.filter(user_id__exact=current_user.id).update(currentScore = data['currentScore'][0])

    return HttpResponse("OK")
