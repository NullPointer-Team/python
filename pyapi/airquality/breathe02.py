import requests



def main():

    r = requests.get(AIR)

    print(r.json())

if __name__ == "__main__":
    main()
