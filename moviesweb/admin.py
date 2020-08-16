from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'imdb_ranking']
    list_filter = ['year', 'imdb_ranking']