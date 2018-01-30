input1 = '1234'
input2 = '0.2'
input3 = 'apple'
input4 = '-2'
import math
def parse(inte):
    try:
        int(inte)
        return int(inte)
    except ValueError:
        return "Not an integer."
print(parse(input1))
print(parse(input2))
print(parse(input3))
print(parse(input4))

print(parse(input1)+parse(input4))

    
