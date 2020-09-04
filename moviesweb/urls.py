from django.urls import path
from django.contrib.auth.decorators import login_required
from moviesweb.views import NewMovieView, EditMovieView, DeleteMovieView, DetailMovieView, NewReviewView,\
    SearchView, SendMessageView, DetailMessageView, AnswerMessageView, DeleteMessageView, AllMoviesView, RegisterView, AllMessagesView

urlpatterns = [
    path('', AllMoviesView.as_view(), name='all_movies'),
    path('new/', login_required(NewMovieView.as_view()), name='new_movie'),
    path('edit/<int:pk>/', login_required(EditMovieView.as_view()), name='movie_edit'),
    path('detail/<int:pk>/', DetailMovieView.as_view(), name='movie_detail'),
    path('detail/<int:pk>/new_review/', NewReviewView.as_view(), name='new_review'),
    path('delete/<int:pk>', login_required(DeleteMovieView.as_view()), name='movie_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('search/', SearchView.as_view(), name='search'),
    path('messages/', login_required(AllMessagesView.as_view()), name='messages'),
    path('messages/send_message', SendMessageView.as_view(), name='send_message'),
    path('messages/answer_message/<int:id>', AnswerMessageView.as_view(), name='answer_message'),
    path('messages/<int:pk>', DetailMessageView.as_view(), name='message_detail'),
    path('messages/delete/<int:pk>', DeleteMessageView.as_view(), name='delete_message'),
]