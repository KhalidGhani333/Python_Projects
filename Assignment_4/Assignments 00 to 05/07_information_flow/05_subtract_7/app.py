
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() 
# method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    if num < 7:
        print("Please Give Greater Number!")
    else:
        return num - 7
    
def main():
    user_number = int(input("Enter a number: "))
    result = subtract_seven(user_number)
    if user_number > 7:
        print("Result after subtracting 7:", result)

main()