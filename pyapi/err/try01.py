while True:
    try:
        print("enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("no problems with that file name")
        break
    except:
        print("error with that file name! Try again....")
