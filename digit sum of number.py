#Digit Sum
x = int(input("Enter the number: "))
sum = 0

while(x != 0):
    sum = sum + round((x % 10))
    x = x/10

print("The sum is: ", sum)