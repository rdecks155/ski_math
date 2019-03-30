from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)

    def __str__(self):
        return self.username

class Game(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    level = models.CharField(max_length=255)

    def __str__(self):
        return self.level

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    games = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.user