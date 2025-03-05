from django.shortcuts import render, redirect
from Base.forms import RegistrationForm, LoginForm
from Base.models import GameResult, PlayerProfile
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model


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


@login_required
def add_score(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            action = data.get('action')

            if action == 'add_point':
                game_result, created = GameResult.objects.get_or_create(user=request.user)
                game_result.score += 1
                game_result.save()
                return JsonResponse({'status': 'success', 'message': 'Очко добавлено'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Недопустимое действие'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Только POST запросы разрешены'}, status=405)