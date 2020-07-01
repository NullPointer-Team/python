import requests



def main():
    r = requests.get(AIR)

    print( dir(r) )

if __name__ == "__main__":
    main()
