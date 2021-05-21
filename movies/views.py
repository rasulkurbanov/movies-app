from movies.models import Genres, Movie
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse("Hello World, You are at my first django project")
    # return HttpResponse(output)
    return render(request, 'movies/base.html', { 'movies': movies })
