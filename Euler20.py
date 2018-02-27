from functools import reduce

def multiply(x):
    y = x-1
    while y>=1:
        x *= y
        y-=1
    return x
    

def numberssum(x):
    sumnum = 0    
    for i in str(multiply(x)): 
        sumnum+=int(i)
    print(sumnum)
numberssum(100) 