from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Rating
from .forms import MovieForm, RatingForm


def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

@login_required
def new_movie(request):
    new = True
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_movies)
    return render(request, 'movie_form.html', {'form': form, 'new': new})

@login_required
def edit_movie(request, id):
    new = False
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect(all_movies)
    return render(request, 'movie_form.html', {'form': form, 'new': new})

@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)
    return render(request, 'confirm.html', {'movie': movie})


def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    ratings = Rating.objects.filter(movie=movie)
    return render(request, 'movie_detail.html', {'movie': movie, 'ratings': ratings})

@login_required
def new_review(request, id):
    movie = get_object_or_404(Movie, pk=id)
    review_form = RatingForm(request.POST or None)
    if request.method == 'POST':
        if 'rating' in request.POST:
            review = review_form.save(commit=False)
            review.movie = movie
            review.save()
            # return redirect(movie_detail(movie.id))
    return render(request, 'review_form.html', {'review_form': review_form, 'movie': movie})

