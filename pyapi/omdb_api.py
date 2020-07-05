import urllib.request
import json


OMDB = "http://www.omdbapi.com/?apikey="



def main():
    with open("../../omdb_api.py") as key:
        api_key = key.read()

    api_creds = api_key.strip("\n")

    api_data = urllib.request.urlopen(OMDB + api_creds + "&t=star+wars")

    core = api_data.read()
    movie_info = json.loads(core.decode("utf-8"))
    title = movie_info['Title']
    year = movie_info['Year']
    rating = movie_info['Ratings'][0]['Value']

    print(title)
    print(year)
    print(rating)


if __name__ == '__main__':
    main()
