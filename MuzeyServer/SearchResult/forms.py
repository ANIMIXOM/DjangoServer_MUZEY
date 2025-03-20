from django import forms
from .models import ImagePerson

class ImagePersonForm(forms.ModelForm):
    class Meta:
        model = ImagePerson
        fields = ['filename']
