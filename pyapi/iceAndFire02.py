import requests
import pprint

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():

    gotresp = requests.get(AOIF_BOOKS)

    #print(gotresp.status_code)

    got_dj = gotresp.json()

    #pprint.pprint(got_dj)


if __name__ == "__main__":
    main()
