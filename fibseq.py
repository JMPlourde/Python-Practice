fibseq = {1:1, 2:1}
def fib(n):
    if n not in fibseq:
        fibseq[n] = fib(n-2)+fib(n-1)
    return fibseq[n]
print(fib(18))
