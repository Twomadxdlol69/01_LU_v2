import random

# main routine goes here
tokens = {"unicorn", "horse", "zebra" "donkey"}
STARTING_BALANCE = 100

# Testing loop to generate 20 tokens
for item in range(0,20):
    chosen = random.choice(tokens)

    # adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
         balance -= 1
    else:
         balance -= 0.5

    # output
    print("token: {} , balance: ${}".format(chosen,balance))