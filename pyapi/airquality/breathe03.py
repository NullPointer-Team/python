import requests



def main():

    r = requests.get(AIR)

    print("Weather Forecast")
    print("----------------")

    for x in r.json():
        print(x.get("DateForecast"))
        print("--------------")
        print(x.get("Discussion"))


if __name__ == "__main__":
    main()
