# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as userlogin
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            userlogin(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

