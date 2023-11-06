# WAP to add 'tion' at the end of a given. {length should be at least 3}, if a given string already ends with tion,
# then add ed instead. if the string length is less than 3 then reverse the input string.

str = input("Enter string: ")

if len(str) >= 3:
    if str.endswith("tion"):
        new_str = str + "ed"
    else:
        new_str = str + 'tion'
else:
    new_str = str[::-1]

print("String after changing:", new_str) 
