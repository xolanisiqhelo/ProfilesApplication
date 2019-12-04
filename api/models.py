from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    productAuthenticationQuestionID = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    answerStatusInd = models.CharField(max_length=50)
    questionPointValue=models.CharField(max_length=50)
    requiredNoOfAnswers=models.CharField(max_length=50)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    answerID = models.CharField(max_length=15)
    answer = models.DateField()
    isEnteredAnswerYN = models.CharField(max_length=255)


