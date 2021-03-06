# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User


@method_decorator(csrf_exempt, name='dispatch')
class Register(View):
    def get(self, request):
        logout(request)
        return render(request, 'accounts/register.html')

    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.create_user(username, password=password)
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)

@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def get(self, request):
        logout(request)
        return render(request, 'accounts/login.html')

    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse(status=400)
        else:
            login(request, user)
            return HttpResponse(status=200)

@method_decorator(csrf_exempt, name='dispatch')
class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')