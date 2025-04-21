import random

secret_number = random.randint(0,99)  # Generate a random number

guess_number = int(input("Enter a guess :"))   # Ask for user input

while guess_number != secret_number:  # Repeat until correct guess
    if guess_number > secret_number:
        print("Your guess is too high ")
    else:
        print("Your guess is too low ")
   
    guess_number = int(input("Enter a new number :")) # Ask for a new guess

print(f"Congrats! The number was: {secret_number}") # End game on correct guess