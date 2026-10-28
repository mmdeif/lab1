import time
from algorithms import pointers, bin_s, point_2, binar2

def times(f, m, n):
    results = []

    for i in range(5):
        start = time.perf_counter()
        f(m, n)
        end = time.perf_counter()
        results.append(end - start)

    return sum(results) / len(results)


M = 10
data=[]

for N in [10, 100, 1000, 10000, 100000, 1000000]:
    m = range(0, 2 * N, 2 * (N // M))
    n = range(1, 2 * N, 2)

    t1 = times(pointers, m, n)
    t2 = times(bin_s, m, n)
    t3 = times(point_2, m, n)
    t4 = times(binar2, m, n)

    data.append([N, t1, t2, t3, t4])
    print([N, t1, t2, t3, t4])
