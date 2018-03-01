from math import sqrt

def divisors(a): #pass 
    properdivisors = []
    for i in range(1, int(sqrt(a)+1)):
        if a%i==0:
            b=int(a/i)
            if b != sqrt(a) and b!= a:
                properdivisors.append(i)
                properdivisors.append(b)
            else: 
                properdivisors.append(i)
    return properdivisors

def sumdivisors(div): #pass properdivisors as div
    total = 0
    for i in div:        
        total += i
    return total    

def amis(known, unknown):
    if sumdivisors(divisors(unknown)) == known and sumdivisors(divisors(known)) ==unknown:
        return True

def sumofamis(n):
    possibilitiesdict = {}
    amicables = []
    for i in range(2,n):
        possibilitiesdict[i] = sumdivisors(divisors(i))
        if sumdivisors(divisors(i)) in possibilitiesdict and amis(i,sumdivisors(divisors(i))) and i!=sumdivisors(divisors(i)) :
                amicables.append(i)
                amicables.append(sumdivisors(divisors(i)))
    print(sum(amicables))
            
sumofamis(10000)