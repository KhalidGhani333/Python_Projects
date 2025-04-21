
# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:
# Asks the user for their first name and stores it in a variable
# Asks the user for their last name and stores it in a variable
# Asks the user for their email address and stores it in a variable
# Returns all three of these pieces of data in the order it was asked
# You can return multiple pieces of data by separating each piece with a comma in the return line.

def get_user_data():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    user_email = input("What is your email address? ")

    if first_name and last_name and user_email:
        return first_name , last_name ,user_email
    else:
        print("Please fill all the input!")

def main():
    user_data = get_user_data()
    print(f"Received the following user data: {user_data}")

main()