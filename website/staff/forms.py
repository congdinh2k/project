from django import forms
from .models import Story, Author, Chap
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = '__all__'


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'email',
            'password1',
            'password2',
        ]


class ChapForm(forms.ModelForm):
    class Meta:
        model =Chap
        fields = '__all__'