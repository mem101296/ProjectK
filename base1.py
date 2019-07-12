#This will eventually be unscripted

def answer(userq): #Function answer

    if userq == "How are you?":
        A_answer = "> I am fine. Thanks."
        return A_answer #returns the answer

    elif userq == "You can't!":
        B_answer = "> Wait what?!" #returns the answer
        return B_answer

    elif userq == "What are your morals":
        C_answer = "> We are programmed to cause no harm to live forms."
        return C_answer

    else:
        D_answer = "> ErRoR... \n> Eeerror \n> Sorry How can I help?"
        return D_answer #returns the answer


print("> Welcome User") #I want this to search a database of welcoming sentences
username = input("> What is your name? \n") #This will search for a way to ask a users name

print("> Hello " + username + "! How can I help?")

userq = input() #Records users question

userqOld = userq #records users answer

print(answer(userq)) #calls function answer

userq = input() #Records users question

if userqOld == userq: #Allows for different output
    print(answer(userq)) #Calls answer function

elif userq == AdmIput:
    print("Welcome to the Admin panel")
    print("Here is the menu:")

else:
    print("end of program")
