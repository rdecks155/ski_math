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
        context = {'student_list': student_data}
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
        # Student.objects.filter(user_id__exact=current_user.id).update(highestScore = data['highestScore'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(addHighestScore = data['addHighestScore'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(subHighestScore = data['subHighestScore'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(recHighestScore = data['recHighestScore'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(addLevel = data['addLevel'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(subLevel = data['subLevel'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(recLevel = data['recLevel'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(highestLevel = data['highestLevel'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(levelHighestScore = data['levelHighestScore'][0])
        # Student.objects.filter(user_id__exact=current_user.id).update(currentScore = data['currentScore'][0])
        if int(data['highestScore'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].highestScore:
            Student.objects.filter(user_id__exact=current_user.id).update(highestScore = data['highestScore'][0])
        if int(data['addHighestScore'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].addHighestScore:
            Student.objects.filter(user_id__exact=current_user.id).update(addHighestScore = data['addHighestScore'][0])
        if int(data['subHighestScore'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].subHighestScore:
            Student.objects.filter(user_id__exact=current_user.id).update(subHighestScore = data['subHighestScore'][0])
        if int(data['recHighestScore'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].recHighestScore:
            Student.objects.filter(user_id__exact=current_user.id).update(recHighestScore = data['recHighestScore'][0])
        if int(data['addLevel'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].addLevel:
            Student.objects.filter(user_id__exact=current_user.id).update(addLevel = data['addLevel'][0])
        if int(data['subLevel'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].subLevel:
            Student.objects.filter(user_id__exact=current_user.id).update(subLevel = data['subLevel'][0])
        if int(data['recLevel'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].recLevel:
            Student.objects.filter(user_id__exact=current_user.id).update(recLevel = data['recLevel'][0])
        if int(data['highestLevel'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].highestLevel:
            Student.objects.filter(user_id__exact=current_user.id).update(highestLevel = data['highestLevel'][0])
        if int(data['levelHighestScore'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].levelHighestScore:
            Student.objects.filter(user_id__exact=current_user.id).update(levelHighestScore = data['levelHighestScore'][0])
        if int(data['currentScore'][0]) > Student.objects.filter(user_id__exact=current_user.id)[0].currentScore:
            Student.objects.filter(user_id__exact=current_user.id).update(currentScore = data['currentScore'][0])
    return HttpResponse("OK")

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def Certificate(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    current_user = request.user
    account_info = Student.objects.filter(user_id__exact=current_user.id)
    print("account info: ", account_info)
    p.drawString(100, 700, "Congratulations! You have played ski math")
    for account in account_info:
        text = "highest score: " + str(account.highestScore)
        p.drawString(100, 600, text)
        text = "addition highest score: " + str(account.addHighestScore)
        p.drawString(100, 575, text)
        text = "subtraction highest score: " + str(account.subHighestScore)
        p.drawString(100, 550, text)
        text = "place recognition highest score: " + str(account.recHighestScore)
        p.drawString(100, 525, text)
        text = "highest level: " + str(account.highestLevel)
        p.drawString(100, 500, text)
        text = "addition level: " + str(account.addLevel)
        p.drawString(100, 475, text)
        text = "subtraction level: " + str(account.subLevel)
        p.drawString(100, 450, text)
        text = "recognition level: " + str(account.recLevel)
        p.drawString(100, 425, text)
        text = "level highest score: " + str(account.levelHighestScore)
        p.drawString(100, 400, text)
        text = "current score: " + str(account.currentScore)
        p.drawString(100, 375, text)

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response