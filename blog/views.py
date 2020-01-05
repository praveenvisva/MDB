from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from .models import Movie, Review
from users.models import Preference


def home(request):
    context = {'movies': Movie.objects.all()}
    return render(request, template_name='blog/home.html', context=context)


class MovieListView(ListView):
    model = Movie
    template_name = 'blog/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'movies'
    ordering = ['-date_added']


class MovieDetailView(DetailView):
    model = Movie


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    context_object_name = 'reviews'
    ordering = ['-date_added']
    allow_empty = False

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Review.objects.filter(movie=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        movie_name = Review.objects.filter(movie=self.kwargs['pk']).first()
        movie_name = movie_name.movie
        context['movie_name'] = movie_name
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        object = self.get_object()
        movie = Movie.objects.filter(id=object.pk).first()
        form.instance.movie = movie
        return super().form_valid(form)


def about(request):
    return render(request, template_name='blog/about.html', context={'title': 'About'})


def toprated(request):
    context = {'toprated': Movie.objects.order_by('-rating')}
    return render(request, template_name='blog/toprated.html', context=context)


@login_required()
def upvote(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.upvote += 1
    movie.save()
    return redirect('blog-home')


@login_required()
def downvote(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.downvote += 1
    movie.save()
    return redirect('blog-home')


def recommendation(request):
    user = request.user
    try:
        preference = Preference.objects.get(user=user)
    except Preference.DoesNotExist:
        preference = None
    if not preference:
        messages.warning(request, "Preference is not set")
        return redirect('preference')
    genre = preference.genres
    context = {'recommendation': Movie.objects.filter(genres=genre).order_by('-rating')}
    return render(request, template_name='blog/recommendation.html', context=context)
