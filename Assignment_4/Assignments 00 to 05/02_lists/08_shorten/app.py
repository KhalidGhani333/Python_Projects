
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list,
#  and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter 
# than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets 
# a list and passes it into your function once you run the program. For the autograder to pass you 
# will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


max_lenght = 3

def shorten(lst):
    while len(lst) > max_lenght:
        remove_item = lst.pop()
        print("Removed:",remove_item)

def main():
    lst = input("Enter a list of items separated by spaces: ").split()
    print("Original list:",lst)

    shorten(lst)
    print("Final List:",lst)

if __name__ == "__main__":
    main()