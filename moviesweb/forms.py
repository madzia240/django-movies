from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'imdb_ranking', 'poster']