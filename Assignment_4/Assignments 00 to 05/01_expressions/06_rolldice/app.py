
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

max_num = 6

def main():
    die1 = random.randint(1,max_num)
    die2 = random.randint(1,max_num)
    total = die1 + die2

    print(f"Die-1: {die1} , Die-2: {die2}")
    print(f"Total : {total}")

if __name__ == "__main__":
    main()