from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import list
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.postgres.search import SearchVector
from .models import Movie, Rating, Message
from .forms import CustomUserCreationForm, SearchForm, MessageForm


class AllMoviesView(list.ListView):
    model = Movie


class NewMovieView(CreateView):
    model = Movie
    fields = ['title', 'year', 'description', 'imdb_ranking', 'poster']


class EditMovieView(UpdateView):
    model = Movie
    fields = ['title', 'year', 'description', 'imdb_ranking', 'poster']
    template_name_suffix = '_update_form'


class DeleteMovieView(DeleteView):
    model = Movie
    success_url = reverse_lazy('all_movies')


class DetailMovieView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        movie = get_object_or_404(Movie, id=self.object.pk)
        kwargs['rating_list'] = Rating.objects.filter(movie=movie)
        return super(DetailMovieView, self).get_context_data(**kwargs)


class NewReviewView(CreateView):
    model = Rating
    template_name = 'moviesweb/rating_form.html'
    fields = ['review', 'rating', 'name', 'movie']

    def get_initial(self):
        movie = get_object_or_404(Movie, id=self.kwargs['pk'])
        name = self.request.user
        return {'movie': movie, 'name': name}


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {"form": CustomUserCreationForm})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("all_movies"))


class SearchView(View):
    form = SearchForm()
    query = None
    results = []

    def get(self, request):
        if 'query' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data['query']
                self.results = Movie.objects.annotate(search=SearchVector(
                    'title', 'description'),).filter(search__icontains=query)
        return render(request, 'search.html', {'search_form': self.form, 'query': self.query, 'results': self.results})


class AllMessagesView(list.ListView):
    model = Message


class SendMessageView(View):
    message_form = MessageForm

    def post(self, request):
        form = self.message_form(request.POST)
        message = form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect('messages')

    def get(self, request):
        form = self.message_form
        return render(request, 'send_message.html', {'message_form': form})


class DetailMessageView(DetailView):
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user == self.object.reciever:
            self.object.readed = True
            self.object.save()
        return context


class AnswerMessageView(View):
    message_form = MessageForm

    def get(self, request, id):
        answering_message = get_object_or_404(Message, pk=id)
        message_form = self.message_form(request.POST or None, initial={
                                   'reciever': answering_message.sender})
        return render(request, 'answer_message.html',
                      {'message_form': message_form, 'answering_message': answering_message})

    def post(self, request):
        message = self.message_form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect('messages')


class DeleteMessageView(DeleteView):
    model = Message
    success_url = reverse_lazy('messages')