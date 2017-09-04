# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import log

# Create your views here.
def ard_login(request,user_id,user_pwd):
    user = models.Login.objects.filter(pk=user_id)
    msg = log.Log()
    msg.write_msg( request.META.get("REMOTE_ADDR")+" try to login")
    if user[0] != None:
        if user[0].user_id == user_id and user[0].user_pwd == user_pwd:
            msg.write_msg(request.META.get("REMOTE_ADDR") + " login success!"+'\n')
            return HttpResponse("true")
    msg.write_msg(request.META.get("REMOTE_ADDR") + " login debeat!"+'\n')
    return HttpResponse("false")

def index(request):
    return HttpResponse("OK")