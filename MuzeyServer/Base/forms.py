from django.forms import TextInput, ModelForm

from .models import Visitor


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['Name', 'Surname']

        widgets = {
            "Name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя",
                "display": "inline - block"
            }),
            "Surname": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Фамилия"
            })
        }
