import requests
import json

API = "https://statsapi.web.nhl.com/api/v1/teams"

def main():
    r = requests.get(API)

    data = r.json()

    teams = data['teams']

    for team in teams:
        print(f"The {team['name']} play in {team['venue']['city']}")

if __name__ == '__main__':
    main()
