from math import sqrt
def trinum(x):
    z = 1 #length of bottom row of dots
    y = 0 #total dots
    factors = 0 #number of factors
    while factors<x:
        factors = 0
        n = 1
        while n<=int(sqrt(y)):
            if y%n==0:
                factors+=2
                n+=1
            else:
                n+=1
        n = 1
        if factors<x:
            y=y+z
            z += 1        
    return y
print(trinum(500))  

            
