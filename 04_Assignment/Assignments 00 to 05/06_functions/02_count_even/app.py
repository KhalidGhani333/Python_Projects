
def count_even():
    numbers  = []

    while True :
        user_input = input("Enter an integer or press enter to stop :")
    
        if user_input == "":
            break
        numbers.append(int(user_input))
    
    even_num = sum(1 for num in numbers if num % 2 == 0 )
    print(f"Number of even numbers: {even_num}")


count_even()