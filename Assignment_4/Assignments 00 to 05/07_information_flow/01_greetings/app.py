

# We've written a helper function for you called greet(name) which takes as input a string name
#  and prints a greeting. Write some code in main() to get the user's name and then greet them,
#  being sure to call the greet(name) helper function.


def greet(name):
    print(f"Greetings {name}!")

def main():
    user_name = input("What's your name? ")
    greet(user_name)

main()