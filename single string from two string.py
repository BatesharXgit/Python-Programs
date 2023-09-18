str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

temp = str1[:2]
str1 = str2[:2] + str1[2:]
str2 = temp + str2[2:]

str3 = str1 + " " + str2
print(str3)
