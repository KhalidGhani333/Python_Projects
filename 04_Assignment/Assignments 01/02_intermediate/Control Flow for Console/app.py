import random

TOTAL_ROUNDS = 5  #total rounds to play

def play_high_low():

    score = 0              #initilized player score

# Loop through all rounds
    for round_num in range(1, TOTAL_ROUNDS + 1):
        print(f"Round {round_num}")

        player_number =random.randint(1,100)      #generate random number for player
        computer_number =random.randint(1,100)    #generate random number for computer

        print(f"Your number is: {player_number}")

        guess = input("Do you think your number is higher or lower than the computer's?: ") # player to guess

        while guess not in ["higher","lower"]:  # validate user input
            guess = input("Please type only 'higher' or 'lower': ")

        # Check if the guess is correct
        is_higher = guess == "higher" and player_number > computer_number
        is_lower = guess == "lower" and player_number < computer_number

        #Checks if the player guessed correctly
        if is_higher or is_lower:
            print(f"Correct! The Computer Number is {computer_number}.")
            score += 1
        else:
            print(f"OOPS! Wrong Guess. The Computer Number was {computer_number}.")
        
        print(f"Correct Your Score is {score}")

    # Game over - give feedback based on final score
    print("\n=== Game Over ===")
    print(f"Your final score: {score}")


    if score == TOTAL_ROUNDS:
        print("Incredible! You got all correct!")
    elif score > TOTAL_ROUNDS // 2:
        print("Well done! You did a good job!")
    else:
        print("Don't worry, you'll get better next time!")

play_high_low()