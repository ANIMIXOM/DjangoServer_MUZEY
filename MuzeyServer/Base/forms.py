import random

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Username",
        max_length=150,
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Имя"
        })
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=150,
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Фамилия"
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isdigit():
            raise ValidationError("Код должен состоять только из цифр")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким кодом уже существует")
        return username

    def save(self):
        while True:
            username = str(random.randint(10000000, 99999999))
            if not User.objects.filter(username=username).exists():
                break
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=8,
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Код"
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                cleaned_data['user'] = user
            except User.DoesNotExist:
                raise ValidationError("Пользователь с таким кодом не найден")
        return cleaned_data
