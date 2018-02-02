from timeit import default_timer as timer

start = timer()

from math import sqrt

def primetest(a):
    for i in range(3, int(sqrt(a)+1)):
        if a % i == 0:
                return False
    return True

def sumofprimes(x):
    total = 0
    for n in range(3,x+1,2):
        if primetest(n):
            total+=n
    if x>=2:
        total+=2
    return total
print(sumofprimes(2000000))

elapsed_time = timer() - start 
print(elapsed_time)