# Shout out to DjangoCentral for posting this fun project for beginners!!!
# https://djangocentral.com/creating-a-guessing-game-in-python/

# This is a number game where the program will pick a number from 1 to 10 and
# will then ask the user to guess the correct number  up to five times!

import random   # Importing random in order to select the target number
number = random.randint(1, 10)  # This will limit the target number between 1 and 10

player_name = input("Hi there! What's your name?  ") 

number_of_guesses = 0   # Starting assignment for our guessing variable.

print("Hey "+ player_name + "! I'm thinking of a number between 1 and 10. Guess what it is!")

while number_of_guesses < 5:    # This loop will expect the player to input a number and then tell them if they are too low or high
                                # It will also limit them to 5 guesses!    
    guess = int(input())
    number_of_guesses += 1 
    
    if guess < number:
        print("You're number is too low!")
    if guess > number:
        print("You're number is too high!")
    if guess == number:
        break
        
        
   
if guess == number: # If the player guesses the number correctly or uses all 5 guesses unsuccessfully...
    print("You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("You did not guess the number! The number was " + str(number))

