

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot.
#  Foot is the singular, and feet is the plural.

inches = 12

def main():
    feet = int(input("Enter Number of Feet :"))

    calculate = inches * feet

    print(f"{feet} Feet is equal to {calculate} Inches")

if __name__ == "__main__":
    main()