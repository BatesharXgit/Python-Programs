#WAP to create a tuple of all values present in a dictionary and find their average

dictionary = {'a': 10, 'b':20, 'c':30, 'd':40, 'e':50}

tupl = ({i: j for d in (dictionary) for i, j in dictionary.items()})
average = (tupl)
print(average)