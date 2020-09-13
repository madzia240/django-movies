from django.contrib import admin
from .models import Movie, Rating, Message, Profile


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'imdb_ranking']
    list_filter = ['year', 'imdb_ranking']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rating']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'reciever', 'msg_text', 'readed']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
