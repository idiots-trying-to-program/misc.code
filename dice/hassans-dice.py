#welcome to the program. This is a dice roll/random number generator program. By SyedHassanHaider
import math
#let's use the math module to make our calculations isn't really required here though. Optional.
import random
#Random module lets us generate random numbers. this is needed to run random.randint to create the dice rolls.
n = random.randint(1, 6)
#randint meaning random interger (1, 6) is the range i.e. 1-6
print("Are you ready to roll your dice? (y/n)")
#Asking the user if they wish to roll their dice.
a = input()
#user input
if a == "y":
#if the user wants to roll their dice
    print("You rolled a " + str(n) + "!")
else: print("Okay, just roll when you're ready.")
#if they don't want to roll their dice
