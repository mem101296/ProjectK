import datetime
import time
import sys

def answer(userq): #Function answer can be called at any point

    if userq == "How are you":
        A_answer = "> I am fine. Thanks."
        return A_answer #returns the answer

    elif userq == "You can't!":
        B_answer = "> Wait what?!" #returns the answer
        return B_answer

    elif userq == "What are your morals":
        C_answer = "> We are programmed to cause no harm to live forms."
        return C_answer

    elif userq == "What can you do":
        D_answer = "> Heres is what I can do? \n\"How are you?\" \n\"You can't\" \n\"What are your morals\" \n\"What can you do\" \n\"Help\""
        return D_answer

    elif userq == "What is todays date":
        now = datetime.datetime.now()
        E_answer = ("> Current date is" + (now.strftime(" %m-%d-%Y")))
        return E_answer

    elif userq == "Help":
        Y_answer = "> Heres is what I can do? \n\"How are you?\" \n\"You can't\" \n\"What are your morals\" \n\"Help\""
        return Y_answer

    else:
        Z_answer = "> ErRoR... \n> Eeerror \n> Sorry How can I help?"
        return Z_answer #returns the answer


#Starting sequence, only said once
print("> Welcome User My Name Is Python") #I want this to search a database of welcoming sentences
username = input("> What is your name? \n") #This will search for a way to ask a users name
print("> Hello " + username + "! How can I help?")

#infinite loop starts Here

while True:

    userq = input() #Records users question

    userqAnswer = userq #records users answer

    if userq == "Good bye":
        print("Please wait while program ends....")
        break

    elif userq =="good bye":
        print("Please wait while program ends....")
        break

    else:
        print(answer(userq)) #calls function according to user answer
        Btext = "...\n"
        for char in Btext:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.4)
        print(">What else can I help you with?")
