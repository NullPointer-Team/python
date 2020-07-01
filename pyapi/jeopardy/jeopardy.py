# using std library method for getting at API data
import urllib.request
import json


# GOBAL / CONSTANT of the API we want to lookup
jeopardy = "http://jservice.io/api/random"

def main():
    counter = 0
    score = 0

    while counter < 10:
        coreData = urllib.request.urlopen(jeopardy)

        #core = coreData.read()
        #print(core)
        # pull STRING data off of the 200 response (even tho it's JSON!)
        xString = coreData.read().decode()
        #print(type(xString))

        # convert STRING data into Python Lists and Dictionaries
        trivia = json.loads(xString)

        question = trivia[0]['question']
        answer = trivia[0]['answer']

        print(question)

        guess = input("\nYour answer: ")
        if (guess == answer.lower()):
            print("you are correct!")
            score += 1
        else:
            print("that is not correct!")
            print("\nthe correct answer was ", answer)

        counter+=1

    print(f"your final score is {score}")

if __name__ == "__main__":
    main()
