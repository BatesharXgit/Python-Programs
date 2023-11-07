#filter function

# filter(function, sequence)

# a = [1,2,3,4,5,6,7,8]
# odd = lambda a: a % 2 != 0
# odd_seq = list(filter(odd, a))
# print(odd_seq)


# def sqr(i):
#     return i * i
# x = map(sqr,(3,5,7))
# print(list(x))

# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(list(x))


from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10,11,12]
x = list(filter(lambda n: n%2==0, l))
y = list(map(lambda x:x*2,x))
z = reduce(lambda x,y: x+y, y)

print(x)
print(y)
print(z)