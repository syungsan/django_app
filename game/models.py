from django.db import models

# Create your models here.
class Score(models.Model):

    userName = models.TextField()
    questionNumber = models.IntegerField()
    question = models.TextField()
    correctAnswer = models.TextField()
    userAnswer = models.TextField()
    responseTime = models.TextField()
