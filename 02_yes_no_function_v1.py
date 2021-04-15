# functions goes here...

def yes_no(question):
    valid = False
    while not valid:
        response = input (question).lower ()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

def instructions():
    print("**** How to Play****")
    print()
    print("the rules of the game go here")
    print()
    return ""
print("please answer yes / no")

# Main routine goes here...
played_before = yes_no("have you played the game before")
if played_before == "no":
        instructions()

print("program continues")

# main routine goes here