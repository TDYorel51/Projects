from random import random


import random
def guess(x):
    number = random.randint(1,x)
    guess = 0
    while guess != number:
        guess = int(input (f"Guess a number from 1-{x}: "))
        if guess > number:
            print("Your number is too high. Try again")
        elif guess < number:
            print("Your number is too low. Try again.")
    else:
        print("You guessed the number correctly!")
guess(10)

