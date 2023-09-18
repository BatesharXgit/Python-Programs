# ax^2 + bx + c = 0
# 2x^2 + 4x + 8 = 0
#quadratic rules can be equal,

import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

d=((b*b)-(4*a*c))

if d > 0:
    print("d=",d)
    print("The roots are real and different.")
    r1=-b+(math.sqrt(d))/ (2 * a)
    r2=-b-(math.sqrt(d)) / (2 * a)
    print("The roots are:",r1,"and",r2)
elif d == 0:
    print("d=",d)
    print("The roots are equal")
    r1=-b+(math.sqrt(d)) / (2 * a)
    r2=-b-(math.sqrt(d)) / (2 * a)
    print("The roots are:",r1,"and",r2)
elif d < 0:
    print("The roots are imaginery.", "The value is: ", d)
