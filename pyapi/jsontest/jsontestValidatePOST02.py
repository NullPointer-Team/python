import requests

TIME = "http://date.jsontest.com"
IP = "http://ip.jsontest.com"
VALID = "http://validate.jsontest.com"


def main():

    response = requests.get(TIME)
    mytime = response.json()

    mytime = mytime["time"].replace(' ', '').replace(":", "-")


    response = requests.get(IP)
    my_ip = response.json()

    print(my_ip)
    my_ip = my_ip["ip"]

    with open("myservers.txt") as myfile:
        myservers = myfile.readlines()




    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = my_ip
    jsonToTest["mysvrs"] = myservers

    mydata = {}
    mydata["json"] = str(jsonToTest)


    response = requests.post(VALID, data=mydata)
    response_json = response.json()

    print(response_json)

    print(f"Is your JSON valid? {response_json['validate']}")

if __name__ == "__main__":
    main()
