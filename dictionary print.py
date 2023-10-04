#WAP to create and print a dictionary where keys are the numbers from 1 to n, and values are pairs of keys

values = dict({})
n = int(input("Enter the values of n: "))
# values[1:n] = input('Enter the values: ')
for i in range(1, n+1):
    values.update({i:i*i})

print(values)