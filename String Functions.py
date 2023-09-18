# String by exchanging the first and last character of given string

# str = input("Enter the string: ")

# last_element = len(str)

# for i in range(len(str)):
#     str = str.replace(str[0], '*')
#     str = str.replace(last_element, '*')
# print(str)

str = input("Enter the string: ")

if len(str) >= 2:
    modified_str = '*' + str[1:-1] + '*'
else:
    modified_str = str

print(modified_str)
