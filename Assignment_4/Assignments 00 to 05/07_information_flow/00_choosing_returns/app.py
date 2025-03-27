


ADULT_AGE = 18
def is_adult(user_age):
    if user_age > ADULT_AGE:
        return True
    
    return False

def main():
    age = int(input("How old is this person? "))
    print(is_adult(age))
main()