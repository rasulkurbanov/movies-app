from django import http
from movies.models import Genres, Movie
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse("Hello World, You are at my first django project")
    # return HttpResponse(output)
    return render(request, 'movies/base.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
