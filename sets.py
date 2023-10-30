s = {1,2,3,4}
s1 = {3,4,5,6}

# s.add(5) # add new element to the set
# print(s)
# s.remove(4) # remove element from set
# print(s)
# s.discard(5) # not give us any error if there is typeerror
# print(s)
# s.clear() #clear all the elements and give empty sets
# print(s)

# s.add(3)
# s.remove(2)
s3 = s.union(s1)
s4 = s.intersection(s1)
s5 = s.difference(s1)
s6 = s1.difference(s)
s7 = s.symmetric_difference(s1)

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
# s4.update(s7)
print(s3)
