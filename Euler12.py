from math import sqrt

def numoffacs(b): #finds number of factors in each (b)
    factors = 0 #number of factors
    n = 1
    while n<=int(sqrt(b)):
        if b%n==0:
            factors+=2
        n+=1
    n = 1
    return factors        

def trinum(x): #increases total number of units y until y is over (x)
   z = 1 #length of bottom row of dots
   y = 0 #total dots  
   while numoffacs(y)<x:
       y=y+z
       z += 1
       print(y)
   return y
print(trinum(500))
