from django.contrib import admin
from .models import Person, ImagePerson
from .forms import ImagePersonForm


class ImagePersonInline(admin.TabularInline):
    model = ImagePerson
    form = ImagePersonForm
    extra = 5


class PersonAdmin(admin.ModelAdmin):
    inlines = [ImagePersonInline]

class ImagePersonAdmin(admin.ModelAdmin):
    form = ImagePersonForm
    list_display = ('person', 'nazvanie')


admin.site.register(Person, PersonAdmin)
admin.site.register(ImagePerson)
