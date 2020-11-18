# GUI-based version of RPSLS

import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    if name == "rock":
        return str(0)
    elif name == "Spock":
        return str(1)
    elif name == "paper":
        return str(2)
    elif name == "lizard":
        return str(3)
    elif name == "scissors":
        return str(4)
    else:
        return "Invalid choice!"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Invalid choice!"


def rpsls(player_choice):
    print " "
    print "Player chooses "+ player_choice
    player_number = int(name_to_number(player_choice))

    comp_number = int(random.randrange(0,4))
    comp_choice = number_to_name(comp_number)
    print "The computer chooses " + comp_choice

    if (player_number-comp_number)%5 == 1:
        print "Player wins!"
    elif (player_number-comp_number)%5 == 2:
        print "Player wins!"
    elif (player_number-comp_number)%5 == 3:
        print "Computer wins!"
    elif (player_number-comp_number)%5 == 4:
        print "Computer wins!"
    elif (player_number-comp_number)%5 == 0:
        print "It's a tie!"
    else:
        print "You have an invalid choice!"



def get_guess(guess):

    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()



# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")