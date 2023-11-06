#WAP to create a list of n colour names and delete all colour names from odd positions of the list, 
#then the print the remaining colour names in reverse.

# n = int(input("Enter no. of colours: "))
# colours = []


# for i in range(n):
#     colour = input("Enter colour: ")
#     colours.append(colour)

# print("All the Colours entered by you", colours)

# for color in reversed(colours):
#     print("Reversed Colour: ", color)


l = input("Enter colour name: " ).split()

del l[::2]

l.reverse()

print([item[::-1]] for item in l)
