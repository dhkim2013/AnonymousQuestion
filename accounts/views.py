# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User


@method_decorator(csrf_exempt, name='dispatch')
class Register(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.create_user(username, password=password)
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)