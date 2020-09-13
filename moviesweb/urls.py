from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from moviesweb.views import NewMovieView, EditMovieView, DeleteMovieView, DetailMovieView, NewReviewView,\
    SearchView, SendMessageView, DetailMessageView, AnswerMessageView, DeleteMessageView, AllMoviesView, RegisterView, \
    AllMessagesView, UserReviewsView, DeleteReviewView, EditReviewView, AccountOptionsView, ProfileEditView

urlpatterns = [
    path('', AllMoviesView.as_view(), name='all_movies'),
    path('new/', login_required(NewMovieView.as_view()), name='new_movie'),
    path('edit/<int:pk>/', login_required(EditMovieView.as_view()), name='movie_edit'),
    path('detail/<int:pk>/', DetailMovieView.as_view(), name='movie_detail'),
    path('detail/<int:pk>/new_review/', NewReviewView.as_view(), name='new_review'),
    path('delete/<int:pk>', login_required(DeleteMovieView.as_view()), name='movie_delete'),
    path('review_delete/<int:pk>', login_required(DeleteReviewView.as_view()), name='review_delete'),
    path('review_edit/<int:pk>/', login_required(EditReviewView.as_view()), name='review_edit'),
    path('register/', RegisterView.as_view(), name='register'),
    path('search/', SearchView.as_view(), name='search'),
    path('messages/', login_required(AllMessagesView.as_view()), name='messages'),
    path('messages/send_message', SendMessageView.as_view(), name='send_message'),
    path('messages/answer_message/<int:id>', AnswerMessageView.as_view(), name='answer_message'),
    path('messages/<int:pk>', DetailMessageView.as_view(), name='message_detail'),
    path('messages/delete/<int:pk>', DeleteMessageView.as_view(), name='delete_message'),
    path('user/', AccountOptionsView.as_view(), name='account_options'),
    path('user/reviews', UserReviewsView.as_view(), name='user_reviews'),
    path('user/password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('user/password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('user/password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('user/password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('user/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('user/edit_profile', login_required(ProfileEditView.as_view()), name='user_profile_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)