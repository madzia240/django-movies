from django.urls import path
from moviesweb.views import all_movies, new_movie, edit_movie, delete_movie

urlpatterns = [
    path('', all_movies, name='all_movies'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>/', edit_movie, name='movie_edit'),
    path('delete/<int:id>', delete_movie, name='movie_delete')
]