str = input('Enter a string: ')

vowels = 'aeiou'

for i in range(len(str)):
    if str[i] in vowels:
        str = str.replace(str[i], '*')

print(str)