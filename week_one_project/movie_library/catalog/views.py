# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html#basic-example-geo-location-api

from django.shortcuts import render
from catalog.models import Movie
import urllib.request
import json

OMDB = "http://www.omdbapi.com/?apikey="

# Create your views here.
def index(request):
    movie = {}

    with open("../../../omdb_api.py") as key:
        api_key = key.read()

    api_creds = api_key.strip("\n")

    api_data = urllib.request.urlopen(OMDB + api_creds + "&t=star+wars")

    core = api_data.read()
    movie_info = json.loads(core.decode("utf-8"))

    print(movie_info['Title'])
    movie = movie_info

    num_movies = Movie.objects.all().count()

    context = {
        'num_movies': num_movies,
        'movie': movie,
    }

    return render(request, 'index.html', context=context)
