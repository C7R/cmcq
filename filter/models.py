from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length= 500)
    optiona = models.CharField(max_length=100)
    optionb = models.CharField(max_length=100)
    optionc = models.CharField(max_length=100)
    optiond = models.CharField(max_length=100)
    correctans = models.IntegerField(default=1)
    selected = models.BooleanField(default=0)                   #0 for not selected, 1 for selected
    #level = models.BooleanField(default=0)                  #0 for FE, 1 for SE TE BE

    def __str__(self):
        a = self.id
        a = str(a)

        return self.question + 'ID :- ' + a


class NewQuestions(models.Model):
    question = models.CharField(max_length= 500)
    optiona = models.CharField(max_length=100)
    optionb = models.CharField(max_length=100)
    optionc = models.CharField(max_length=100)
    optiond = models.CharField(max_length=100)
    correctans = models.IntegerField(default=1)
    #selected = models.BooleanField(default=0)                   #0 for not seen, 1 for seen
    level = models.BooleanField(default=0)                  #0 for FE, 1 for SE TE BE
    def __str__(self):
        a = self.id
        a = str(a)

        return self.question + 'ID :- ' + a


class Player(models.Model):
    pid = models.OneToOneField(User, on_delete= models.CASCADE)
    pname = models.CharField(max_length=44)
    sid = models.IntegerField(default=0)
    cid = models.IntegerField(default=0)
    eid = models.IntegerField(default=0)
    #questseen = models.IntegerField(default=0)

    def __str__(self):
        return self.pname



