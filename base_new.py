import datetime
import time
import sys


def help():
    help_answer = (
        "> How are you?\n"
        "> What are your morals?\n"
        "> What can you do?\n"
        "> What is todays date?\n"
        "> What time is it?\n"
        "> What is my name?\n"
        "> Help\n"
    )
    return help_answer


def answer(userq):  # Function answer can be called at any point

    if userq == "How are you":
        A_answer = "< I am fine. Thanks."  # Assigns variable
        return A_answer  # returns answer or variable

    elif userq.lower().find("cant") >= 0:
        B_answer = ("< Fine!")  # Assigns variable
        return B_answer  # returns answer or variable

    elif userq.lower().find("your morals") >= 0:
        C_answer = "< We are programmed to cause no harm to life forms."
        return C_answer

    elif userq == "What can you do":
        D_answer = ("< Heres is what I can do!" + help())
        return D_answer

    elif userq == "What is todays date":
        now = datetime.datetime.now()  # Assigns now to date and time
        E_answer = ("< Current date is" + (now.strftime(" %m-%d-%Y")))  # Assigns time to variable
        return E_answer  # returns answer or variable

    elif userq == "What time is it":
        now = datetime.datetime.now()  # Assigns now to date and time
        F_answer = ("< Current time is" + (now.strftime(" %l:%M%p %z")))  # Assigns time to variable
        return F_answer  # returns answer or variable

    elif userq.lower().find("my name") >= 0:
        G_answer = ("< Your name is " + username)  # Assigns time to variable
        return G_answer  # returns answer or variable

    elif userq.lower().find("help") >= 0:  # help command
        Y_answer = ("< Heres what you can say!\n" + help())
        return Y_answer

    else:
        Z_answer = "< ErRoR... \n> Eeerror \n> Sorry How can I help?"
        return Z_answer  # returns the answer


Stext = "\nStarting Python......\n"  # Starting sequence, only said once
Satext = "Executing ProjectK.py......\nLoading"
Sbtext = "..........\n\n"
for char in Stext:  # starts a loop based on whats in Btext
    sys.stdout.write(char)  # prints out by each character
    sys.stdout.flush()  # Changes the pase of output
    time.sleep(0.1)  # amount it takes for it to print

for char in Satext:  # starts a loop based on whats in Btext
    sys.stdout.write(char)  # prints out by each character
    sys.stdout.flush()  # Changes the pase of output
    time.sleep(0.1)  # amount it takes for it to print

for char in Sbtext:  # starts a loop based on whats in Btext
    sys.stdout.write(char)  # prints out by each character
    sys.stdout.flush()  # Changes the pase of output
    time.sleep(0.6)  # amount it takes for it to print


print("######## ProjectK ########")  # Welcome sequence
print("< Welcome User My Name Is ProjectK")  # I want this to search a database of welcoming sentences
username = input("< What is your name? \n> ")  # This will search for a way to ask a users name

# Figure out how to filter names only, find only returns numbers

while len(username) == 0:
    username = input("< What is your name? \n> ")  # This will search for a way to ask a users name

print("< Hello " + username + "! How can I help?\n")

# infinite loop starts Here

while True:

    userq = input("> ")  # Records users question!

    userqAnswer = userq  # records users answer

    if userq.lower().find("bye") >= 0:  # ends program if Good bye is typed
        print("< Please wait while program ends....")
        break

    elif userq.lower().find("cant") >= 0:
        print(answer(userq))
        break

    elif userq.lower() == "exit":
        print("< Good bye!")
        break

    else:
        Btext = "\n< ...\n"
        for char in Btext:  # starts a loop based on whats in Btext
            sys.stdout.write(char)  # prints out by each character
            sys.stdout.flush()  # Changes the pase of output
            time.sleep(0.4)  # amount it takes for it to print
        print(answer(userq))  # calls function according to user answer
        print("\n> What else can I help you with?")
