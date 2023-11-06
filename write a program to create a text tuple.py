# write a program to create a text tuple by reading a line of text user then generate a length tuple of this same 
#size where each integer value represents the length of the corresponding word.

# line = input("Enter your line: ")
# whitespace = ' '
# length = 0

# if whitespace in line:
#     text = line.split()

# for i in text:
#     length = [text.count(i)]

# print(text)
# print(length)

line = input("Enter your line: ")

text = line.split()
length = tuple(len(i) for i in text)

print("Text:", text)
print("Length:", length)