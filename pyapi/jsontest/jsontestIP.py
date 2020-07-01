import requests

API = "http://ip.jsontest.com"

def main():
    response = requests.get(API)

    response_json = response.json()

    print(response_json)

    print(f"The current WAN IP is --> {response_json['ip']}")

if __name__ == "__main__":
    main()
