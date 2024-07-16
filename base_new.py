"""These modules provide access to datetime and sys, such as stdout"""

import datetime
import time
import sys


def help_output():
    """Fuction outputing what questions are valid"""
    print(
        "> How are you?\n"
        "> What are your morals?\n"
        "> What can you do?\n"
        "> What is todays date?\n"
        "> What time is it?\n"
        "> What is my name?\n"
        "> Help\n"
    )


def answer(user_question):
    """Function with answers to question in help"""
    now = datetime.datetime.now()
    answer_dict = {
        "How are you": "< I am fine. Thanks.",
        # find.("cant"):"< Fine!",
        # find.("your morals"):"< To follow the rules of Robots and AI!",
        "What can you do":"< Here is what I can do!" + help_output(),
        "What is todays date":"< Current date is: " + (now.strftime(" %m-%d-%Y")),
        "What time is it":"< Current time is: " + (now.strftime(" %l:%M%p %z")),
        # find.("my name"):"< Your name is " + username,
        # find.("help"):"< Heres what you can ask:" + help()

    }
    return answer_dict.get(user_question, error())


def error():
    """Outputs error if nothing matches in dict function"""
    print("< ErRoR... \n How can I help?")


def exit_program():
    """This exits the program"""
    sys.exit(0)

S_TEXT = "\nStarting Python......\n"  # Starting sequence, only said once
S_ATEXT = "Executing ProjectK.py......\nLoading"
S_BTEXT = "..........\n\n"
for char in S_TEXT:  # starts a loop based on whats in Btext
    sys.stdout.write(char)  # prints out by each character
    sys.stdout.flush()  # Changes the pase of output
    time.sleep(0.)  # amount it takes for it to print

for char in S_ATEXT:  # starts a loop based on whats in Btext
    sys.stdout.write(char)  # prints out by each character
    sys.stdout.flush()  # Changes the pase of output
    time.sleep(0.1)  # amount it takes for it to print

for char in S_BTEXT:  # starts a loop based on whats in Btext
    sys.stdout.write(char)  # prints out by each character
    sys.stdout.flush()  # Changes the pase of output
    time.sleep(0.6)  # amount it takes for it to print


print("######## ProjectK ########")  # Welcome sequence
# I want this to search a database of welcoming sentences
print("< Welcome User My Name Is ProjectK")
username = input("< What is your name? \n> ")  # This will search for a way to ask a users name

# Figure out how to filter names only, find only returns numbers

while len(username) == 0:
    username = input("< What is your name? \n> ")  # This will search for a way to ask a users name

print("< Hello " + username + "! How can I help?\n")

# infinite loop starts Here

while True:

    userq = input("> ")  # Records users question!

    userqAnswer = userq.lower()  # records users answer

    if userq.lower().find("bye") >= 0:  # ends program if Good bye is typed
        print("< Please wait while program ends....")
        exit_program()

    elif userq.lower().find("cant") >= 0:
        print(answer(userq))

    elif userq.lower() == "exit":
        print("< Good bye!")
        exit_program()

    else:
        B_TEXT = "\n< ...\n"
        for char in B_TEXT:  # starts a loop based on whats in Btext
            sys.stdout.write(char)  # prints out by each character
            sys.stdout.flush()  # Changes the pase of output
            time.sleep(0.4)  # amount it takes for it to print
        print(answer(userq))  # calls function according to user answer
        print("\n> What else can I help you with?")
