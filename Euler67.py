from timeit import default_timer as timer
 
start = timer()

def from_file(filename):
    tree_list = []
    # Read the tree from a file
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            row = []
            for a in line.strip().split(' '):
                row.append(int(a))
            tree_list.append(row)
    return tree_list

triangle = from_file('p067_triangle.txt')

def comparison(n,m):
    print(n)
    for i in range(len(n)-1):
        if n[i] >= n[i+1]:
            n[i]=n[i]+triangle[m-1][i]
        elif n[i+1] > n[i]:
            n[i]=n[i+1]+triangle[m-1][i]
        
    n.pop()
    return n

def trimax():
    y = -1
    products = triangle[y]
    while len(products)>=2:
        products = comparison(products,y)
        y-=1
    print(products)

trimax()

elapsed_time = timer() - start 
print(elapsed_time)