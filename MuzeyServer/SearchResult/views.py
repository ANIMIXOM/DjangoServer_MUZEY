from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Person

def result(request, ids):
    es_Person = get_object_or_404(Person, id=ids)

    rest = {
        "name": es_Person.full_name,
        "biography": es_Person.biography,
        "image_main":es_Person.image_main,
        "images": es_Person.images.all()
    }
    for p in es_Person.images.all():
        print(p)

    if not rest['images']:
        rest['images'] = ["static/assets/images/Изображение отсутствует.png"]

    return render(request, "page1.html", context=rest)