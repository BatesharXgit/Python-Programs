price = int(input("Enter the price of the product: "))

if price >= 1000:
    discount = price * (10/100)
    amount = price - discount
    final_price = amount
else:
    final_price = price

print("The price of the product after discount is", final_price)

print("=======================================================================")
print("=======================================================================")

x = int(input("Enter a number: "))

if x > 0:
    print("Positive")
elif x < 0:
    print("negative")
else:
    print("Zero")

print("=======================================================================")
print("=======================================================================")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for voting.")
elif age < 18 and age > 0:
    print("You are not eligible for voting.")
else:
    print("You are not born yet!")