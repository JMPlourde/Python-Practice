#What is the 10 001st prime number?

def primetest(a):
    y = 2
    while y*y <= a:
        if a % y == 0:
            return False
        y+=1
    return True

def findprime(n):
    primefac = []
    x = 2
    count = 0
    while count < n:
        if primetest(x):
            primefac.append(x)
            count += 1
        x+=1
    return max(primefac)
print(findprime(6))
print(findprime(10001))
