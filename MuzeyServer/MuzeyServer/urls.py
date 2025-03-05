"""
URL configuration for MuzeyServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SearchMenu.views import menu
from SearchResult.views import result
from GamesList.views import game_bar, game_render, video_render
from Base.views import register_visitor, home, logout_view, login_view, add_score
from send_email.views import send_email

urlpatterns = [
    path("email/", send_email,  name='email'),
    path('admin/', admin.site.urls),
    path('search/<str:name>/', menu),
    path('games/', game_bar),
    path('game/<int:id>', game_render),
    path('register/', register_visitor, name='register'),
    path('', home, name='home'),
    path('result/<int:ids>/', result, name='result'),
    path('video/<int:id>', video_render),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name='login'),
    path('add_score/', add_score, name='add_score'),

]
