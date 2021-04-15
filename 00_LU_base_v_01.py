import random
# functions go here...


def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


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

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play****")
    print()
    print("chose a starting amount (minimum $1, maximum $10."
          "Then press <enter> ro play. You will get either a horse, a zebra, a donkey or a unicorn."
          "it costs a $1 per round. Depending on your prize")
    print()
    return ""


def num_check(question, low, high):

    error = "please enter an whole number between 1 and 10\n"
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response
                # output an error
            else:
                print(error)

        except ValueError:
            print(error)
# main routine goes here...
statement_generator("Welcome to the lucky unicorn game", "*")
print()

played_before = yes_no("have you played this game  before ")

if played_before == "no":
    instructions()
    print()
if played_before == "yes":
    print("Lets play!")

# ask user how much they want to play with
how_much = num_check("how much would you"
                     "like to play with?", 0, 10)


# set balance for testing purposes
balance = how_much
rounds_played = 0
play_again = input("press <Enter> to play...").lower()

while play_again == "":
    # increase # of rounds played
    rounds_played += 1
    # print round number
    print("*** round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        prize_decoration = "!"
        balance += 4
        # if the random # is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "Donkey"
        prize_decoration = "D"
        balance -= 1
        # the token  is either a horse or zebra...
        # in both cases, subtract $0.50 from the balance
    else:

        balance -= 0.5

        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "Horse"
            prize_decoration = "H"
            # otherwise set it to a zebra
        else:
            chosen = "Zebra"
            prize_decoration = "Z"

    outcome = "you got a {}. your balance is " \
        "${:.2f}".format(chosen, balance)
    statement_generator(outcome, prize_decoration)

    print()

    if balance <= 1:
        play_again = "xxx"
        print("sorry you have run out of money")
        print("final balance", balance)
    else:
        play_again = input("press enter to play again " "or 'xxx' to quit")
