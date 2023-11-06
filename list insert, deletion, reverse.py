#WAP to create a list of n colour names and delete all colour names from odd positions of the list, 
#then the print the remaining colour names in reverse.

n = int(input("Enter the number of colors: "))

colours = []

for i in range(n):
    colour = input("Enter color: ")
    colours.append(colour)

colours = [colours[i] for i in range(len(colours)) if i % 2 != 0]
print("Colours after odd deletion: ", colours)

print("Reversed colour:")
# for color in reversed(colours):
#     print(color)

reversedColour = colours.reverse()

print(reversedColour)
