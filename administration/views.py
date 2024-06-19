from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from administration.forms import RegisterForm, LoginForm

# Create your views here.

def register(request):
    # register view
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect('home')
    context = {'form': register_form, 'title': 'Register'}
    return render(request, 'administration/register.html', context)


def login_view(request):
    # login view
    if request.user.is_authenticated:
        return redirect('home')
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    context = {'form': login_form, 'title': 'Register'}
    return render(request, 'administration/login.html', context)


def logout_view(request):
    # logout view
    logout(request)
    return redirect('home')
