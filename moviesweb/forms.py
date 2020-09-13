from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Rating, Message, Profile, User


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'imdb_ranking', 'poster']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'rating']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class SearchForm(forms.Form):
    query = forms.CharField()


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['reciever', 'msg_text']


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
