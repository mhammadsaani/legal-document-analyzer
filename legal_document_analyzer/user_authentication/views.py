from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import HostSignUpForm, LoginForm, SetPasswordCustomForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'authentication/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = HostSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Account already exists')
            else:
                user = form.save()
                messages.success(request, 'Account created successfully')
    form = HostSignUpForm()
    return render(request, 'authentication/sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/doc/upload/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = SetPasswordCustomForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully')
            return HttpResponseRedirect('/auth/login/')
    else:
        form = SetPasswordCustomForm(user=request.user)
    return render(request, 'authentication/change_password.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')


def unauthorized(request):
    return render(request, 'authentication/unauthorized.html')