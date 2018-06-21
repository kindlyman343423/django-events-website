from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    else:
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',
                              {'error': 'Username has already been registered!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                                                email=request.POST['email'],
                                                password=request.POST['password'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/signup.html',
                          {'error': 'Passwords must match!'})


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Username or Password is incorrect!'})


def logout(request):
    auth.logout(request)
    return redirect('index')
