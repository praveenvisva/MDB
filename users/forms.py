from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Preference


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PreferenceForm(forms.ModelForm):
    OPTIONS = [("Action", "Action"), ("Thriller", "Thriller"), ("Sci-Fi", "Sci-Fi"),
               ("War", "War"), ("Romance", "Romance"), ("Drama", "Drama")]
    genres = forms.MultipleChoiceField(
        choices=OPTIONS, widget=forms.CheckboxSelectMultiple(), required=True)

    class Meta:
        model = Preference
        fields = ["genres"]
