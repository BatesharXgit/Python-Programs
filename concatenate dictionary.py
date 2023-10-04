#wap TO CONCATENATE THE to create a new dictionary

d1 = {1: 11, 2: 22, 3: 33}
d2 = {4: 44, 5: 55, 6: 66}
d3 = {7: 77, 8: 88, 9: 99}

dict1 = {**d1, **d2, **d3}

print(dict1)

# d1 = {1: 11, 2: 22, 3: 33}
# d2 = {4: 44, 5: 55, 6: 66}
# d3 = {7: 77, 8: 88, 9: 99}

# dict1 = {i: j for d in (d1, d2, d3) for i, j in d.items()}

# print(dict1)



