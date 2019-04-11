from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)

    def __str__(self):
        return self.username

# class Game(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
#     level = models.CharField(max_length=255, default=None)
#     high_score = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.level

class Student(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # games = models.ForeignKey(Game, on_delete=models.CASCADE, default=0)
    highestScore = models.PositiveIntegerField(default=0)
    addHighestScore = models.PositiveIntegerField(default=0)
    subHighestScore = models.PositiveIntegerField(default=0)
    recHighestScore = models.PositiveIntegerField(default=0)
    highestLevel = models.PositiveIntegerField(default=0)
    addLevel = models.PositiveIntegerField(default=0)
    subLevel = models.PositiveIntegerField(default=0)
    recLevel = models.PositiveIntegerField(default=0)
    levelHighestScore = models.PositiveIntegerField(default=0)
    currentScore = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.user.username