category_1 = {"A", "B", "C", "D"}
category_2 = {"D", "E", "F", "G"}
category_3 = {"D", "H", "I", "J"}

x = category_1.intersection(category_2)
common = x.intersection(category_3)

y = category_1.symmetric_difference(category_2)
unique = y.symmetric_difference(category_3)

print("Common is: ", common)
print("Unique Data is: ", unique)