import requests
import pprint

def main():

    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value':'http for humans'})
    print(f"Status Code - {r.status_code}")
    pprint.pprint(r.json())

    print('*********/n')

    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans'})
    print(f"Status Code - {r.status_code}")

    pprint.pprint(r.json())

if __name__ == "__main__":
    main()
