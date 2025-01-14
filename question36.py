## Guess the Number (Game): The program should generate a random number between 1 and 10. The user guesses until they get it right.

import random

def guess_the_number():
    number = random.randint(1, 10)
    guess = None

    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("You guessed it! You won!")

guess_the_number()