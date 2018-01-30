#Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

sumsquares = 0
def difference(x):
    def sumsquare(x):
        for i in range(1,x):
            sumsquares += i**2
    def squareofsum(x):
        a = x
        b = 0
        while a>0:
            b += a
            a -= 1
        return b**2
    return sumsquares
print(difference(100))