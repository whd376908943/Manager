# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as userlogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            userlogin(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    return render(request, 'login.html')


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def user_manage(request):
    user_list = User.objects.all()
    return render(request, 'user/user_manage.html', {'userList': user_list})


def user_active(request):
    id = request.POST.get('userid')
    state = int(request.POST.get('state'))
    user = User.objects.get(id=id)
    if state:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    print user.username
    return HttpResponse('finish')


def user_del(request):
    id = request.POST.get('userid')    
    user = User.objects.get(id=id)
    print user.username
    user.delete()
    return HttpResponse('finish')



