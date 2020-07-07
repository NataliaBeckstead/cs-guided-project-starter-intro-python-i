# GUESS THE NUMBER!

"""
Assumptions:

Plan:

Features:
- Might look at collect user input about game settings (min, max of random number, number of guesses alllowed, etc.)
- Might look at a different logic for replaying versus playing for the first time
"""

# Need to import the random module
import random

is_playing = True
# Need the main game while loop
while is_playing:
    # give game start message to user that explanes the game and what is ecxpected
    print("Welcome to GUESS THE NUMBER! I hope you have fun!")
    # 
    # initialize a andom number at the start of the game
    number_to_guess = random.randint(1, 100)

    user_has_won = False
    # need a guessing loop that runs until user guesses correctly (while loop&)
    while not user_has_won:
        # prompt the user for their input
        user_guess = int(input("I'm thinking of a number between 1 and 100. Guess whichnumber I'm thinking of: "))
        # TODO: provide data to the user about the game (number of guesses so far?)
        # TODO: do some error checking on the user input

        # if user guess is right
        if user_guess == number_to_guess:
            user_has_won = True
            # program alerts user that guess was wrong if it was too high or too low
            print("YOu guessed right! Good job!")

            play_again = input("Whould you like to play againg? Y or N?")
            if play_again.lower() == "n":
                is_playing = False
        # if user guess is wrong
        elif user_guess > number_to_guess:
            print("Your guess was too high! Try again!")
        else:
            print("Your guess was too low! Try again!")
            # program alerts user they won and asks if they want to play again or exit