import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters"

def main():

    got_charToLookUp = input("What is the name of the character we should look up? ")

    gotresp = requests.get(AOIF_CHAR + "?name=" + got_charToLookUp)

    got_dj = gotresp.json()

    print(got_dj)
    print(f"The character {got_charToLookUp} has the URL: {got_dj[0]['url']}")

if __name__ == "__main__":
    main()
