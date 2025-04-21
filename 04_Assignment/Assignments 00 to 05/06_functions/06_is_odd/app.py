

# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def odd_even():
    num1 = int(input("Enter number for Start :"))
    num2 = int(input("Enter number to End :"))

    for i in range(num1,num2):
    
        if i % 2 == 0 :
            print(f"Even {i}", end=" ")
        else:
            print(f"Odd {i}", end=" ")

odd_even()