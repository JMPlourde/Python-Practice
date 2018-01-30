#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143

def primetest(n):
    y = 2
    while y*y <= n:
        if n % y == 0:
            return False
        y+=1
    return True


def findprime(a):
    primefac = []
    x = 2
    while x*x <= a:
        if a % x == 0:
            if primetest(x) == True:
                primefac.append(x)
            if primetest(a/x) == True:
                primefac.append(int(a/x)) 
        x+=1
    print(max(primefac))

findprime(600851475143)
findprime(46)