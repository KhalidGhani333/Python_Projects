
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit.
#  The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

def print_ones_digit(num):
    ones_digit = num % 5

    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: ")) 
    print_ones_digit(num)

main()