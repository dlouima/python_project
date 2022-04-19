from curses.ascii import HT
from django.shortcuts import render, get_list_or_404
from django.shortcuts import HttpResponse, Http404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):

    movie = get_list_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
