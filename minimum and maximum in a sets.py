#WAP to find minimum and maximum in a set

sets = {1,2,3,4}
sets1 = {4,6,7,8}
sets2 = {4,6,9,10}

# x = sets.isdisjoint(sets1)
x = sets.intersection(sets1)
y = sets2.intersection(x)

print(y)