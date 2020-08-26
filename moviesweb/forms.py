from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Rating


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'imdb_ranking', 'poster']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'rating', 'name']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields