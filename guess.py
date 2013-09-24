from random import randint

def get_and_validate_input():
    player_guess = raw_input("> ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
        if player_guess not in range(1,100):
            print "Your guess must be an integer between 1-100."
            get_and_validate_input()
    else:
        print "Your guess is invalid. Please type a positive integer between 1 and 100."
        get_and_validate_input()
    return player_guess

#greet player and get player name
player_name = raw_input("Hi there. What's your name? ")
#choose random number between 1 and 100
winning_number = randint(1, 100)
print "Let's play a game, %s. I'm thinking of a number between 1 and 100 inclusive. Can you guess what it is? You only get 10 tries!" % player_name

wrong = True
number_of_tries = 0
tries_allowed = 10
guess_again = "Guess again."
tries = "tries"

while wrong and number_of_tries < tries_allowed:
    player_guess = get_and_validate_input()

    number_of_tries += 1
    if number_of_tries == tries_allowed:
        guess_again = "No more guesses!"
    
    tries_left = tries_allowed - number_of_tries

    if winning_number > player_guess:
        print "Your number is too small! %s" % guess_again
        print "You have %d tries left." % (tries_left)
    elif winning_number < player_guess:
        print "Your number is too big! %s" % guess_again
        print "You have %d tries left." % (tries_left)
    else:
        print "%s, you win! Great job!" % player_name
        wrong = False

if wrong:
    print "You lose!"
else:
    if number_of_tries == 1:
        tries = "try"
    print "You guessed the number in %d %s." % (number_of_tries, tries)
