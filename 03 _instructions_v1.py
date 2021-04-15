# functions goes here...
import instructions as instructions


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
            if show_instructions == "yes":
                show_instructions ()
                print("program continues")

    def instructions ():
        print("**** how to play ****")
        print()
        print("the rules of the game go here")
            return  ""
    print("please answer yes / no")

#Main routine goes here...
show_instructions = yes_no("have you played thhe game before")

print("you chose {}").format (show_instructions)

