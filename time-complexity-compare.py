"""
The time complexity comparison between algorithm DPC and the currently best-performing general-purpose maximum flow algorithm.

The time complexity of the algorithm DPC is $nk(nk+2^k)$.
The time complexity of the currently best-performing general-purpose maximum flow algorithm is $O(|E|^{1+o(1)})$, where $E$ denotes the edge number of the network.

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
        return f(n, k) * w(n, k-1)



for n in range(2,9):
    for k in range(2,9):
        a = E(n, k)
        b = n * k * (n * k + pow(2, k))
        print("n=" + str(n) + ", k=" + str(k) + ":")
        if a > b:
            print("The algorithm DPC is more efficiency!")
        else:
            print("The algorithm DPC is not efficiency!")
        print("----------------------------")


