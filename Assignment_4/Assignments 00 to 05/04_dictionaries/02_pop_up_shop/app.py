
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time,
#  you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits
#  were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of
#  each fruit they want to buy, and then prints out the total combined cost of all of the fruits.


def main():
    fruits = {"apple":2 ,"banana":1 ,"orange":3,"pineapple":5,"mango":2}
    total_cost = 0

    for fruit in fruits:
        amount = fruits[fruit]
        fruit_quantity = int(input(f"How many {fruit} do you want?"))
        total_cost += amount * fruit_quantity

    print(f"Your total is {total_cost}")

if __name__ == "__main__":
    main()