#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

print(16*9*5*7*11*13*17*19)

from math import gcd
from functools import reduce
leastmultiple = lambda a,b: int(a*b/gcd(a,b))
def lcm(x):
    return reduce(leastmultiple,x) 
print(lcm(range(1,20)))