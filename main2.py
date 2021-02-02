#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number = 5
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == number: print("Great job! You got it!")
number2 = 4
if guess == number2: print("You are getting very warm, almost there! ")
else: print("Sorry, better luck next time, you are too cold.")
print("The number was " + str(number))