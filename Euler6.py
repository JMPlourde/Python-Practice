#Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

def sumofsquares(x):
    sumsquares = 0
    for i in range(1,x+1):
        sumsquares += i**2
    return sumsquares

def squareofsum(x):
    a = x
    b = 0
    while a>0:
        b += a
        a -= 1
    return b**2

def difference(x):
    return squareofsum(x) - squareofsum(x) 
print(difference(10))
