# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Login(models.Model):
    user_id = models.CharField(max_length=40,primary_key=True)
    user_pwd = models.CharField(max_length=40)