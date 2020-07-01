import requests

URL = "http://validate.jsontest.com"

def main():

    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}"}

    response = requests.post(URL, data = mydata)

    response_json = response.json()

    print(f"Is your JSON valid? {response_json['validate']}")

if __name__ == "__main__":
    main()
