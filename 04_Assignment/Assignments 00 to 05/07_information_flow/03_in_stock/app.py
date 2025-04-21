
def num_in_stock(fruit):
    if fruit == "apple":
        return 50
    elif fruit == "banana":
        return 30
    elif fruit == "pear":
        return 70
    elif fruit == "mango":
        return 25
    else:
        return 0
    
def main():
    user_input = input("Enter a fruit: ")
    stock = num_in_stock(user_input)

    if stock > 0 :
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

main()