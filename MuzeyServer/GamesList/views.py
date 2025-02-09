from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
@login_required(login_url='/login/')
def game_bar(request):
    return render(request, "page3.html")

@login_required(login_url='/login/')
def game_render(request, id):
    return render(request, f"game_{id}.html")

@login_required(login_url='/login/')
def video_render(request, id):
    return render(request, f"video_r{id}.html") #video_r3 заменить на video_r{id}
