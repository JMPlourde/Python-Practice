      
def trinum(x):
    addthings = lambda a,b: a+b
    z = 1 #length of bottom row of dots
    y = 0 #total dots
    factors = 0 #number of factors
    while factors<x:
        factors = 0
        n = 1
        while n<=y:
            if y%64==0 and y%3==0 and y%5==0 and y%7==0 and y%11==0:
                if y%n==0:
                    factors+=1
                    n+=1
                else:
                    n+=1
            else:
                n+=1
        print("botdots", z)
        print("dots", y)
        print("factors",factors)
        if factors<x:
            y=y+z
        n = 1
        z += 1
    return y
print(trinum(500))       