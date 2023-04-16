def respond(message):
    respones = ("Hello", "Cat", "Dog")
    end = 0
    name = "I don't know your name"
    while end == 0:
        userInput = input("Input: ")
        split = userInput.split()
        if ((userInput == "Bye") or (userInput == "bye") or (userInput == "Good Bye") or (userInput == "good bye")):
            end = 1
            print("Good Bye")
        elif ((split[0] == "my") and (split[1] == "name")):
            name = split[3]
            print("Hello " + name)
        elif userInput == "name":
            print(name)
        elif userInput in respones:
            responseMessage = respones[userInput]
            print(responseMessage)
        else:
            responseMessage = "I don't unstand"
            print(responseMessage)

    
            
respond("Hello")
