# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as userlogin
from django.contrib.auth import logout as userlogout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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
@permission_required('auth.change_user', login_url='/noperm/')
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


def user_add(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print username, email, password
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.save()
        return HttpResponse('用户创建成功!')
    else:
        return HttpResponse('用户名已存在!')


def user_info(request, userid):
    user = User.objects.get(id=userid)
    return render(request, 'user/user_info.html', {'user_info': user})


def user_change(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    is_superuser = request.POST.get('is_superuser')
    user = User.objects.get(username=username)
    user.set_password(password)
    user.email = email
    if int(is_superuser):
        user.is_superuser = True
    else:
        user.is_active = False
    user.save()
    return HttpResponse('change success!')


def noperm(request):
    return render(request, 'noperm.html')


def logout(request):
    userlogout(request)
    return redirect('/login')



