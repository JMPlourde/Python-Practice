from timeit import default_timer as timer

start = timer()


from math import sqrt
def pythtrip(n):
    for x in range(1, int((n+1)/2)):
        for y in range(x, int((n+1)/2)):
            for z in range(y, int((n+1))):
                if  x+y+z == n and x**2 + y**2 == z**2:
                    print(x*y*z)
pythtrip(1000)


elapsed_time = timer() - start 
print(elapsed_time)

