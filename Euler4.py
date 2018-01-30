#A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []
for n in range(100,1000):
    for m in range (100,1000):
        x=m*n
        string = str(x)
        reverse = string[::-1]
        if str(x) == reverse:
            palindromes.append(x)
print(max(palindromes))
