from django import forms
from .models import *


class News(forms.ModelForm):
    head = forms.CharField(min_length=2, widget=forms.Textarea(attrs={'rows': 1, 'cols': 100}), label='Заголовок')
    posts = forms.CharField(min_length=10, widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}), label='Статья')
    class Meta:
        model = Post
        fields = ['author', 'link_category', 'head', 'posts']
