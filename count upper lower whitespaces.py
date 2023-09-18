# count all lower case, upper case, whitespace, and special characters in a given string.

# str = "Hello there! How are you."
str = input("Enter your string: ")

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_characters = '!@#$%^&*'
white_spaces = ' '

lower_count = 0
count_upper = 0 
count_spaces  = 0
count_characters = 0

for i in range(len(str)):
    if str[i].islower():
    # if str[i] in lower_case:
        lower_count += 1
    if str[i].isupper():
    # if str[i] in upper_case:
        count_upper += 1
    if str[i] in white_spaces:
        count_spaces += 1
    if str[i] in special_characters:
        count_characters += 1

print(str)
print(lower_count)
print(count_upper)
print(count_characters)
print(count_spaces)

