from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=64)
    passwd = models.CharField(max_length=64)