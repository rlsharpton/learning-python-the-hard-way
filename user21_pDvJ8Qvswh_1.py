# Rock-paper-scissors-lizard-Spock template
# Student - Robin S. 
# I joined class two days before this assignment
# was due. Sorry it is very incomplete.

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "Please enter a number 0,1,2,3, or 4"
        start()
    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif number == 'lizard':
        return 3
    elif number == 'scissors':
        return 4
    else:
        print "Please enter a name"
        start()

def rpsls(name): 
    # fill in your code below
    print "the name is ", name
    
    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

def dead():
    print "there was an error. Sorry we are going."
    exit(0)
    
def start():
    print "Player please choose from the following options: "
    print "rock, Spock, paper, lizard, scissors"
    choice = raw_input('--> ')
    rpsls(choice)
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


