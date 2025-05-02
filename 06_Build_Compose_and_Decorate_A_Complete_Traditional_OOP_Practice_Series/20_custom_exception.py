

# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises 
# this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18 :
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Access granted.")

try :
    user_age = int(input("Enter Your Age "))
    check_age(user_age)

except InvalidAgeError as e:
    print(f"Invalid age Error :{e}")