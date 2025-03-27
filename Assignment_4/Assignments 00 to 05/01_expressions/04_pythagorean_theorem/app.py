import math

def main():
    ab = int(input("Enter the Lenght of AB :"))
    ac = int(input("Enter the Lenght of AC :"))

    bc = math.sqrt(ab ** 2 + ac ** 2)
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

if __name__ == "__main__":
    main()