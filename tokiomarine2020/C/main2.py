import copy
from functools import lru_cache
#import numpy as np
#from numba import njit

def resolve():
    N, K = map(int, input().split())
    #A = np.array(list(map(int, input().split())))
    A = list(map(int, input().split()))

    #N = 2 * 10**5
    #K = 2 * 10**5
    #A = np.array([0] *  N)

    def func(A):
        B = [0] * N
        for i in range(N):
            l = max(0, i - A[i])
            r = min(i + A[i], N-1)
            B[l] += 1
            if r+1 < N:
                B[r+1] -= 1

        for i in range(1, N):
            B[i] += B[i-1]
        return B

    for k in range(K):
        #print(k)
        A = func(A)
        if k >= 50:
            break

    print(" ".join(map(str, A)))

if __name__ == "__main__":
    resolve()