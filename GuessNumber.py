import random

hidden = random.randrange(1, 100)

guess = int(input("Please guess the number:\n"))

if guess == hidden:
    print("Bravo! Correct. ")
elif guess < hidden:
    print("Guess is too low. ")
elif guess > hidden:
    print("Guess is too high. ")

print("The real random number was: " + str(hidden))



