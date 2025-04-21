

minimum_height = 50

def main():
    user_height = int(input("How tall are you? "))

    if user_height >= minimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
 

if __name__ == '__main__':
    main()