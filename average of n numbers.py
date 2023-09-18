#Take n inputs from the user and then calculate their average

n = int(input("Enter the number you want to take as input: "))
total = 0

for i in range(n):
    x = float(input(f"Enter number {i+1} : "))
    total += x

average = total / n
print("The average is: ", average)
