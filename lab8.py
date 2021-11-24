# Program : Number guessing...
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right

import random

#print(random.randrange(1,9))

number = random.randrange(1,9)
guess_a_number = int(input("Please guess a number between 1 and 9:"))

if(guess_a_number not in range(1,9)):
    print("Only between 1 and 9 is allowed!")
elif(number == guess_a_number):
    print("You have guessed exactly right number!!")
elif(number<guess_a_number):
    print("You have guessed too high number") 
elif(number>guess_a_number):
    print("You have guessed too low number")
