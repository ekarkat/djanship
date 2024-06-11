from django.shortcuts import render, redirect

from administration.forms import RegisterForm

# Create your views here.

def register(request):
    # register view
    register_form = RegisterForm()
    context = {'form': register_form, 'title': 'Register'}
    return render(request, 'register.html', context)
