from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.postgres.search import SearchVector
from .models import Movie, Rating, Message
from .forms import MovieForm, RatingForm, CustomUserCreationForm, SearchForm, MessageForm


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


def new_review(request, id):
    movie = get_object_or_404(Movie, pk=id)
    review_form = RatingForm(request.POST or None)
    if request.method == 'POST':
        if 'rating' in request.POST:
            review = review_form.save(commit=False)
            review.movie = movie
            review.name = request.user
            review.save()
            return redirect('movie_detail', id=movie.id)
    return render(request, 'review_form.html', {'review_form': review_form, 'movie': movie})


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("all_movies"))


def movie_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Movie.objects.annotate(search=SearchVector('title','description'),).filter(search__icontains=query)
    return render(request, 'search.html', {'search_form': form, 'query': query, 'results': results})


def messages(request):
    messages = Message.objects.all()
    inbox_messages = Message.objects.filter(reciever=request.user).order_by('-id')
    sentbox_messages = Message.objects.filter(sender=request.user).order_by('-id')
    return render(request, 'messages.html', {'messages': messages, 'inbox_messages': inbox_messages, 'sentbox_messages': sentbox_messages})


def send_message(request):
    message_form = MessageForm(request.POST or None)
    if request.method == 'POST':
        message = message_form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect('messages')
    return render(request, 'send_message.html', {'message_form': message_form})


def message_detail(request, id):
    message = get_object_or_404(Message, pk=id)
    return render(request, 'message_detail.html', {'message': message})


def answer_message(request, id):
    answering_message = get_object_or_404(Message, pk=id)
    message_form = MessageForm(request.POST or None, initial={'reciever': answering_message.sender})
    if request.method == 'POST':
        message = message_form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect('messages')
    return render(request, 'answer_message.html', {'message_form': message_form, 'answering_message': answering_message})


def delete_message(request, id):
    is_message = True
    message = get_object_or_404(Message, pk=id)
    if request.method == 'POST':
        message.delete()
        return redirect(messages)
    return render(request, 'confirm.html', {'message': message, 'is_message': is_message})