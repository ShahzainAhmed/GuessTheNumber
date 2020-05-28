# Importing random module.
import random

# Setting a range of random numbers from 1 to 100. 
hidden = random.randrange(1, 100)   


# Taking input from the user. 
guess = int(input("Please guess the number:\n"))   


# Using if else statements to make conditions.
if guess == hidden:
    print("Bravo! Correct. ")
elif guess < hidden:
    print("Guess is too low. ")
elif guess > hidden:
    print("Guess is too high. ")
    
    
# Using print statement to print the original random number which you had to guess. xD 
print("The real random number was: " + str(hidden))
