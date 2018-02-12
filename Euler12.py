from math import sqrt

def numoffacs(a,b):
    factors = 0 #number of factors
    while factors<a:
        factors = 0
        n = 1
        while n<=int(sqrt(b)):
            if b%n==0:
                factors+=2
            n+=1
        n = 1
        return factors        

def trinum(x):
    z = 1 #length of bottom row of dots
    y = 0 #total dots  
    while numoffacs(x,y)<x:
        y=y+z
        z += 1
        print(y)
    return y
print(trinum(500))  
        
