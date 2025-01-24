from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
def game_bar(request):
    return render(request, "page3.html")


def game_render(request, id):
    return render(request, f"game_{id}.html")


def video_render(request, id):
    return render(request, f"video_r{id}.html") #video_r3 заменить на video_r{id}
