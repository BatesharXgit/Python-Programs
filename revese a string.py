str = input('Enter a string to check palindrome: ')

for i in range(len(str)):
    print(str[i])

str1 = ''.join(reversed(str))

if str == str1:
    print("Palindrome")
else:
    print("Not Palindrome")
