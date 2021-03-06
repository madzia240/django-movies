from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=False)
    year = models.PositiveSmallIntegerField(default=2000, null=True, blank=False)
    description = models.TextField(default="")
    imdb_ranking = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.year})'

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.pk})


class Rating(models.Model):
    review = models.TextField(default="", blank=True)
    rating = models.PositiveSmallIntegerField(default=5)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review added by {self.name}'

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.movie.pk})


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='reciever', on_delete=models.CASCADE)
    msg_text = models.TextField(default='', blank=True)
    readed = models.BooleanField(default=False)
    sended = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'message from {self.sender} to {self.reciever}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'User {self.user}'

