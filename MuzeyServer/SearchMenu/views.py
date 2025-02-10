from django.shortcuts import render
from SearchResult.models import Person

def menu(request, name):
    all_Person = Person.objects.all()
    persons = {}
    if name != "-":
        if name == "ltz":
            all_Person = Person.objects.filter(nazvanie="LTZ")
        if name == "shz":
            all_Person = Person.objects.filter(nazvanie="SCHZ")
        if name == "mas":
            all_Person = Person.objects.filter(nazvanie="Mashzavod")
        if name == "agz":
            all_Person = Person.objects.filter(nazvanie="Agregatny_zavod")
        if name == "shv":
            all_Person = Person.objects.filter(nazvanie="Shveynaya_fabrika")
        if name == "oez":
            all_Person = Person.objects.filter(nazvanie="OEZ")
        if name == "ldk":
            all_Person = Person.objects.filter(nazvanie="Ludinovokabel")
        if name == "xlb":
            all_Person = Person.objects.filter(nazvanie="HleboKombinat")

    for i in all_Person:
        persons[str(i.id)] = i.full_name
    persons = dict(sorted(persons.items(), key=lambda item: item[1]))
    print(persons)
    return render(request, "page2.html", context={"persons": persons})
