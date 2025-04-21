

# Write a function that takes two numbers and finds the average between the two.


def avg_fun(num1,num2):

    sum = (num1 + num2) / 2 
    return sum
    
number1 = int(input("Enter First Number :"))
number2 = int(input("Enter Second Number :"))

average  = avg_fun(number1,number2)
print(f"The Average is {average}")


