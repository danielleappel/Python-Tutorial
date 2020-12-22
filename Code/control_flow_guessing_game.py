# This is my code!
# It's purpose is to demonstrate how control structures work using try/except loops
# and a hosts a game using a while loop

import time
import random

def host_game():

    #1. Get user's name.
    name = input("What is your name? ")
    time.sleep(0.5)
    print("Hello, %s" %name)

    #2. See how many guesses the user would like.
    while True:
        time.sleep(0.7)
        try:
            guesses = int(input("Enter the number of guesses you would like to have. The fewer guesses, the harder the game:\n"))
            break
        except ValueError:
            print("Could not convert the input to an integer. Please enter another integer.")
    
    time.sleep(0.5)
    print("ԅ|.͡° ڡ ͡°.|ᕤ")
    time.sleep(0.5)
    print("Let's get guessing! You have %d guesses.\n" %guesses)
    time.sleep(0.5)

    #3. Initialize the secret number and game status
    secret_num = random.randint(1,10)
    correct = False

    #4. Begin guessing
    while guesses > 0 and (~ correct):
        try:
            time.sleep(0.5)
            curr_guess = int(input("\nPlease enter an integer from 1 to 10:\n"))
            time.sleep(0.5)
        except ValueError:
            print("Could not convert the input to and integer. Please enter another integer:\n")
        time.sleep(0.5)
        if curr_guess == secret_num:
            correct = True
            time.sleep(0.5)
            print("You guessed it! %d is the correct number.\n" %secret_num)
            time.sleep(0.5)
            break
        else:
            guesses -= 1
            print("Incorrect. You have %d guess(es) left." %guesses)
    time.sleep(0.7)
    
    #5. End the game, but first, if the user has lost, alert them now that the game loop is over
    if (~ correct) == -1:
        print("You lost the game. The right number was %d." %secret_num)
        return
    else:
        return

def main():
    host_game()

if __name__ == "__main__":
    main()
