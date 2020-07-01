# using std library method for getting at API data
import urllib.request
import json


# GOBAL / CONSTANT of the API we want to lookup
jeopardy = "http://jservice.io/api/random"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    # context = ssl._create_unverified_context()
    coreData = urllib.request.urlopen(jeopardy)

    #core = coreData.read()
    #print(core)
    # pull STRING data off of the 200 response (even tho it's JSON!)
    xString = coreData.read().decode()
    #print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    trivia = json.loads(xString)
    #print(type(listOfCores))

    question = trivia[0]['question']
    answer = trivia[0]['answer']

    print(question)

    guess = input("\nYour answer: ")
    if (guess == answer):
        print("you are correct!")

if __name__ == "__main__":
    main()
