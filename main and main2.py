#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number = 5
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == number:
    print("Great job! I'm honestly surprised you got that. ")
else:
    print("Wow you are really bad at this, try again. ")
    print("The number was " + str(number))