num = int(input('Enter a number: '))

smallest_num=num % 10

while (num != 0):
    digit = num % 10
    if (digit < smallest_num):
      smallest_num = digit
    num=int(num/10)

print("Smallest number: ", smallest_num)