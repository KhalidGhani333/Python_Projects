

counts = {}

while True:
    num  = input("Enter a number (or press Enter to finish): ")
    
    if num == "":
        break

    num = int(num)
    counts[num] = counts.get(num,0) + 1


for num,counts in counts.items():
    print(f"{num} appears {counts} times.")