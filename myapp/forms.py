from django import forms
from .models import Blog, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['user' ,'title', 'content', 'Image']

class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'user']
        