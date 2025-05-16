from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render,redirect

from accounts.forms import UserForm, LoginForm
from accounts.models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
        return render(request,'accounts/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=CustomUser.objects.filter(username=username).first()
            if user:
                if check_password(password,user.password):
                    login(request,user)
                    return redirect('book-list')
            else:
                return HttpResponse('Invalid username or password')

    else:
        form = LoginForm()
        return render(request,'accounts/login_form.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')