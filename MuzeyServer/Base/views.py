from django.shortcuts import render, redirect
from Base.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def register_visitor(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logi = login_view(request)
            return render(request, 'index.html',
                          {"form": form,
                           'logout_message': f"Ваш код: {user.username}. Запомните или запишите.",
                           "login": logi})
    else:
        form = RegistrationForm()
    return render(request, 'register_visitor.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            if user:
                if user.is_superuser:
                    return redirect('/admin')
                login(request, user)
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
        else:
            return redirect('/register')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
