#https://www.digitalocean.com/community/tutorials/how-to-display-data-from-the-digitalocean-api-with-django
import os
import requests

def get_movies():
    with open("../../../../omdb_api.py") as key:
        api_key = key.read()

    api_creds = api_key.strip("\n")

    url = 'http://www.omdbapi.com/?apikey=' + api_creds + '&s=star'
    #print(url)
    r = requests.get(url)
    movies = r.json()
    movie_list = []
    #print(movies['Search'])
    #print(len(movies['Search']))
    #print('\n')
    #print(movies[0])
    for i in range(len(movies['Search'])):
        movie_list.append(movies['Search'][i])

    return movie_list
