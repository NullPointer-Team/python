import requests
import json

URL = "http://validate.jsontest.com"


def main():

    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}
    jsonToValidate = f"json={ json.dumps(mydata).replace(' ', '') }"

    response = requests.get(f"{URL}?{jsonToValidate}")

    response_json = response.json()

    print(response_json)

    print(f"Is your JSON valid? {response_json['validate']}")

if __name__ == "__main__":
    main()
