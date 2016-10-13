#coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Pageview(models.Model):
    dtime = models.CharField(max_length=64)
    city = models.CharField(max_length=128)
    count = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
	
    def __str__(self):
        return self.city