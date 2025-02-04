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
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = RegistrationForm()
    return render(request, 'register_visitor.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')


def logout_view(request):
    user = request.user
    logout(request)
    form = LoginForm(request.POST)
    logi = login_view(request)
    if user.is_authenticated:
        return render(request, 'login.html',
                      {"form": form, 'logout_message': f"Ваш код: {user.username}. Вы вышли из системы", "login": logi})
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
