

Peturksbouipo_age = 16
Stanlau_age = 25
Mayengua_age = 48

def main():
    age = int(input("Enter Your Age :"))

    if age >= Peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo_age}")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo_age}")

    if age >= Stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {Stanlau_age}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {Stanlau_age}")

    if age >= Mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {Mayengua_age}")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {Mayengua_age}")
    
if __name__ == '__main__':
    main()