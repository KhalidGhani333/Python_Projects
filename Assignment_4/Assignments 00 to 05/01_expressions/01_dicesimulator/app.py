
# Simulate rolling two dice, three times. Prints the results of each die roll. 
# This program is used to show how variable scope works.

import random

max_num = 6

def roll_dice():

    die1 = random.randint(1,max_num)
    die2 = random.randint(1,max_num)
    print(f"Roll : {die1},{die2}")

def main():
    for _ in range(3):
        roll_dice()

if __name__ == "__main__":
    main()
