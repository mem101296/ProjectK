#This will eventually be unscripted
#Infinite loop needs to be created for user input ln32

def answer(userq): #Function answer can be called at any point

    if userq == "How are you?":
        A_answer = "> I am fine. Thanks."
        return A_answer #returns the answer

    elif userq == "You can't!":
        B_answer = "> Wait what?!" #returns the answer
        return B_answer

    elif userq == "What are your morals":
        C_answer = "> We are programmed to cause no harm to live forms."
        return C_answer

    elif userq == "Help":
        D_answer = "> Heres is what I can do? \n\"How are you?\" \n\"You can't\" \n\"What are your morals\" \n\"Help\""
        return D_answer

    else:
        Z_answer = "> ErRoR... \n> Eeerror \n> Sorry How can I help?"
        return Z_answer #returns the answer


print("> Welcome User My Name Is Python") #I want this to search a database of welcoming sentences
username = input("> What is your name? \n") #This will search for a way to ask a users name

print("> Hello " + username + "! How can I help?")

#Create loop below

userq = input() #Records users question

userqAnswer = userq #records users answer

print(answer(userq)) #calls function according to user answer

userq = input() #Records users question

"""if userqAnswer == userq: #Allows for different output
    print(answer(userq)) #Calls answer function"""

"""elif userq == AdmIput:
    print("Welcome to the Admin panel")
    print("Here is the menu:")"""

"""else:
    print("end of program")"""
