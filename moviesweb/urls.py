from django.urls import path
from moviesweb.views import all_movies, new_movie, edit_movie, delete_movie, movie_detail, new_review

urlpatterns = [
    path('', all_movies, name='all_movies'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>/', edit_movie, name='movie_edit'),
    path('detail/<int:id>/', movie_detail, name='movie_detail'),
    path('new_review/<int:id>/', new_review, name='new_review'),
    path('delete/<int:id>', delete_movie, name='movie_delete'),
]