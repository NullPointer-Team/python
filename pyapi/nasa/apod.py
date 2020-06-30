import urllib.request
import json


NASA = "https://api.nasa.gov/planetary/apod?"

def main():

    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()


    nasacreds = "api_key=" + nasacreds.strip("\n")

    apodurlobj = urllib.request.urlopen(NASA + nasacreds)

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
