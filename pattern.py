x = int(input("Enter the length of the triangle: "))

for i in range(x):
    print(" "*(x-i)+"* "*i)
for i in range(x, 0, -1):
    print(" "*(x-i)+"* "*i)