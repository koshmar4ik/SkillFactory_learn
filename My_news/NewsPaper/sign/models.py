from django.db import models

# Create your models here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            group, _ = Group.objects.get_or_create(name="common")
            user.groups.add(group)
        return user
