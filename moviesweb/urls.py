from django.urls import path
from moviesweb.views import all_movies, new_movie, edit_movie, delete_movie, movie_detail, new_review, register, \
    movie_search, messages, send_message, message_detail, answer_message, delete_message

urlpatterns = [
    path('', all_movies, name='all_movies'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>/', edit_movie, name='movie_edit'),
    path('detail/<int:id>/', movie_detail, name='movie_detail'),
    path('new_review/<int:id>/', new_review, name='new_review'),
    path('delete/<int:id>', delete_movie, name='movie_delete'),
    path('register/', register, name='register'),
    path('search/', movie_search, name='search'),
    path('messages/', messages, name='messages'),
    path('messages/send_message', send_message, name='send_message'),
    path('messages/answer_message/<int:id>', answer_message, name='answer_message'),
    path('messages/<int:id>', message_detail, name='message_detail'),
    path('messages/delete/<int:id>', delete_message, name='delete_message'),
]