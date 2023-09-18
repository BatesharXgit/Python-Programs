#write a program to remove all the characters other than integers from a given string

str = input("Enter your string: ")

new_str = ""

for i in str:
    if i.isdigit():
        new_str += i

print(new_str) 
