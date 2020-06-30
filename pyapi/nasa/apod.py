import urllib.request
import json
import ssl


NASA = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("nasa_creds.py") as mycreds:
        nasacreds = mycreds.read()


    nasacreds = "api_key=" + nasacreds.strip("\n")

    context = ssl._create_unverified_context()

    apodurlobj = urllib.request.urlopen(NASA + nasacreds, context=context)

    apodread = apodurlobj.read()

    apod = json.loads(apodread.decode("utf-8"))

    print("\n\nConverted Python Data")

    print(apod)

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])



if __name__ == "__main__":
    main()
