from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Base.models import GameResult


# @login_required
@login_required(login_url='/login/')
def game_bar(request):
    f = False
    user_id = request.user.id
    responce = GameResult.objects.filter(user_id=user_id)
    responce = responce[0]
    if responce.score >= 5:
        f = True
    return render(request, "page3.html", {'f': f})


@login_required(login_url='/login/')
def game_render(request, id):
    return render(request, f"game_{id}.html")


@login_required(login_url='/login/')
def video_render(request, id):
    return render(request, f"video_r{id}.html")  # video_r3 заменить на video_r{id}
