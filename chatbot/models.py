from django.db import models


class User(models.Model):
    name = models.CharField(max_length=25)


class Chat(models.Model):

    username = models.CharField(max_length=25)
    message = models.TextField(max_length=200, null=True, blank=True)
    isuser = models.BooleanField()
