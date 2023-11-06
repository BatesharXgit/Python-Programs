x = int(input('Enter the value of X: '))
y = int(input('Enter the value of Y: '))
z = int(input('Enter the value of Z: '))

if x > y and x > z:
    print("X is greater than Y and Z")
elif y > x and y > z:
    print("Y is greater than X and Z")
elif z > x and z > y:
    print("Z is greater than X and Y")
else:
    print(":)")
