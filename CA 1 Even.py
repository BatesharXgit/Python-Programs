# Find the sum of squares of middle three digits of a 5 digit entered by the user. if the count of the digits in the entered 
#number is not 5, then find the product of all the digits

x = input("Enter a number with 5 digits: ")

if len(x) == 5 and x.isdigit():
    middle = x[1:4]
    squareSum = sum(int(digit) ** 2 for digit in middle)
    print("Sum of squares of middle three digits: ", squareSum)
else:
    product = 1
    for digit in x:
        if digit.isdigit():
            product *= int(digit)
    print("Product of all digits: ", product)