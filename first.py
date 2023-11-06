import sys
import math

# Numeric Types => int, float, complex
# Sequence Types => String, list, tuple
# Boolean Types => True/False
# Set 
# Dictionary

#operators => Arithmetic, relational, logical(and, or, not), bitwise, assignment, Identity(boolean), Membership(in, not in) 

x = int(input('Enter the value of X: ')) # user input and converting that to integer
y = 20

print(x)
print(type(y)) #for printing the type of variables

print('The size of X is: ', sys.getsizeof(x))  # to get the size of variables
print('The size of Y is: ', sys.getsizeof(y))
print("The square root of the number is: ", round(math.sqrt(x)))

if x > y:
    print("Hey!")
elif x == y:
    print("Whats's up")
elif x < y:
    print("That's cool")
else:
    print(":)")

for i in range(1, 11):
    print(i * 2, end=" ")