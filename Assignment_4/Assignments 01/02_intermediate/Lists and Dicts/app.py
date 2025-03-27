
# access the element
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index Out of Range"

# modify the element
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index Out of Range"

# slicing the element
def slice_list(lst, start, end):
    try:
        return lst[start : end]
    except IndexError:
        return "Index Out of Range"

# add the element
def add_element(lst, new_value):
    try:
        lst.append(new_value)
        return lst
    except IndexError:
        return "Index Out of Range"

# delete the element
def delete_element(lst, index):
    try:
        del lst[index]
        return lst
    except IndexError:
        return "Index Out of Range"

def index_game():
    lst = ["apple", "banana", "orange", "grape", "pineapple"]  
    print("Current list:", lst)

    # user operation
    print("Choose operation: access, modify, slice, add, delete, exit")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter Index to access :"))
        print(access_element(lst,index))

    elif operation == "modify":
        index = int(input("Enter Index to modify :"))
        new_value = input("Enter new value: ")
        print(modify_element(lst,index,new_value))

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst,start,end))

    elif operation == "add":
        new_value = input("Enter new value: ")
        print(add_element(lst,new_value))

    elif operation == "delete":
        index = int(input("Enter index to delete elemet: "))
        print(delete_element(lst,index))

    elif operation == "exit":
        print("Exiting the game. Goodbye!")
        breakpoint

    else:
        print("Invalid operation!")

index_game()
