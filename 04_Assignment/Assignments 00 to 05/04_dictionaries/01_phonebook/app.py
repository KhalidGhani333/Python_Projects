
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

phonebook = {}

while True:
    user_name = input("Name:")
    if user_name == "":
        break
    number = input("Number:")
    phonebook[user_name] = number

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

while True:
    name  = input("Enter name to lookup: ")
    if name == "":
        break
    if name not in phonebook:
        print(name + " is not in the phonebook")
    else:
        print(phonebook[name])