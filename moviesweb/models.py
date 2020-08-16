from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=False)
    year = models.PositiveSmallIntegerField(default=2000, null=True, blank=False)
    description = models.TextField(default="")
    imdb_ranking = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.year})'