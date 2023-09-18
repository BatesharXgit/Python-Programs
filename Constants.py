import Constants

r = int(input("Enter the radius: "))
pi = (22/7)

area = (Constants.pi * (r * r))
permimeter = (2 * Constants.pi * r)

print("The area and perimeter of circle using constant is: ",round(area, 2),"and", round(permimeter, 2), "respectively.")
