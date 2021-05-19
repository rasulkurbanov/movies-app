from django.contrib import admin
from .models import Genres, Movie

# Register your models here.
class GenresAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "daily_rate", "genre")

admin.site.register(Genres, GenresAdmin)
admin.site.register(Movie, MovieAdmin)
