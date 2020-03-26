import datetime
import time
import sys

def answer(userq): #Function answer can be called at any point

    if userq == "How are you":
        A_answer = "> I am fine. Thanks." #Assigns variable
        return A_answer #returns answer or variable

    elif userq == "You cant!":
        B_answer = ("> Fine!") #Assigns variable
        return B_answer #returns answer or variable

    elif userq == "What are your morals":
        C_answer = "> We are programmed to cause no harm to live forms."
        return C_answer

    elif userq == "What can you do":
        D_answer = "> Heres is what I can do! \n•How are you? \n•You cant! \n•What are your morals \n•What can you do \n•Help"
        return D_answer

    elif userq == "What is todays date":
        now = datetime.datetime.now() #Assigns now to date and time
        E_answer = ("> Current date is" + (now.strftime(" %m-%d-%Y"))) #Assigns time to variable
        return E_answer #returns answer or variable

    elif userq == "What time is it":
        now = datetime.datetime.now() #Assigns now to date and time
        F_answer = ("> Current time is" + (now.strftime(" %l:%M%p %z"))) #Assigns time to variable
        return F_answer #returns answer or variable

    elif userq == "Help": #help command
        Y_answer = "> Heres is what I can do? \n\"How are you?\" \n\"You can't\" \n\"What are your morals\" \n\"Help\""
        return Y_answer

    else:
        Z_answer = "> ErRoR... \n> Eeerror \n> Sorry How can I help?"
        return Z_answer #returns the answer


#Starting sequence, only said once
Stext = "Starting Python......\n"
SWtext = "......\n"
for char in Stext: #starts a loop based on whats in Btext
    sys.stdout.write(char) #prints out by each character
    sys.stdout.flush() #Changes the pase of output
    time.sleep(0.1) #amount it takes for it to print

for char in SWtext: #starts a loop based on whats in Btext
    sys.stdout.write(char) #prints out by each character
    sys.stdout.flush() #Changes the pase of output
    time.sleep(0.1) #amount it takes for it to print
#Welcome sequence
print("> Welcome User My Name Is Python") #I want this to search a database of welcoming sentences
username = input("> What is your name? \n") #This will search for a way to ask a users name
print("> Hello " + username + "! How can I help?")

#infinite loop starts Here

while True:

    userq = input() #Records users question

    userqAnswer = userq #records users answer

    if userq == "Good bye": #ends program if Good bye is typed
        print("Please wait while program ends....")
        break

    elif userq =="good bye": #ends program if good bye is typed
        print("Please wait while program ends....")
        break

    elif userq == "You cant!":
        print(answer(userq))
        break

    else:
        Btext = "> ...\n"
        for char in Btext: #starts a loop based on whats in Btext
            sys.stdout.write(char) #prints out by each character
            sys.stdout.flush() #Changes the pase of output
            time.sleep(0.4) #amount it takes for it to print
        print(answer(userq)) #calls function according to user answer
        print("> What else can I help you with?")
