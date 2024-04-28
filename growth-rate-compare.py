"""
The growth rate comparsion between the execution time of algorithm DPC and the scale of $D_{n,k}$.

The time complexity of the algorithm DPC is $nk(nk+2^k)$.
The scale of $D_{n,k}$ is represented by the number of edges in $D_{n,k}$.
The number of edges in $D_{n,k}$ is $|E(D_{n,k})|=|E(D_{n,k-1})|*f_k+\frac{f_k(f_k-1)}{2}$,
where $k\geq 1$, $f_k=n*w_{k-1}+1$ denotes the number of disjoint copies $D_{n,k-1}$ in $D_{n,k}$, $w_k=f_k*w_{k-1}$ denotes the number of nodes in $D_{n,k}$, and $|E(D_{n,0})|=0$.
"""

def E(n, k):
    if k == 0:
        return 0
    else:
        return E(n, k-1) * f(n, k) + f(n, k) * (f(n, k) - 1) / 2

def f(n, k):
    return n * w(n, k-1) + 1

def w(n, k):
    if k == 0:
        return 1
    else:
        return f(n,k)*w(n,k-1)

for n in range(2,9):
    for k in range(2,9):
        # n varied and k fixed
        a1 = E(n, k) / E(n-1, k) - 1
        b1 = (n * k * (n * k + pow(2, k))) / ((n-1) * k * ((n-1) * k + pow(2, k))) - 1
        # n fixed and k varied
        a2 = E(n, k) / E(n, k-1) - 1
        b2 = (n * k * (n * k + pow(2, k))) / (n * (k-1) * (n * (k-1) + pow(2, k-1))) - 1
        print("n=" + str(n) + ", k=" + str(k) + ":")
        if a1 > b1 and a2 > b2:
            print("The algorithm DPC is sublinear!")
        else:
            print("The algorithm DPC is not sublinear!")
        print("----------------------------")


