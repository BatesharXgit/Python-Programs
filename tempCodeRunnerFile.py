age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for voting.")
elif age < 18 and age > 0:
    print("You are not eligible for voting.")
else:
    print("You are not born yet!")