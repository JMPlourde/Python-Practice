#What is the 10 001st prime number?
def prime(y):
    while x <=y:
        x = 1
        primes = {}:
        primes[x] = primetest()
        x+=1
    print(primes(y))

def primetest(n):
    y = 2
    while y*y <= n:
        if n % y == 0:
            return False
        y+=1
    return n
