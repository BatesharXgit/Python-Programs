# WAP to print all the prime numbers line in the range m to n entered by the user, where m and n both are inclusive

m = int(input("Enter the lower bound: "))
n = int(input("Enter the upper bound: "))

if m > n:
    m, n = n, m

print("Prime numbers between ", m, "and", n, "is: ")
for number in range(m, n, +1):
    if number > 1:
        isPrime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                isPrime = False
                break
        if isPrime:
            print(number, end=" ")