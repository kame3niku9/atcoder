import math
from functools import lru_cache
from operator import mul
from functools import reduce


def resolve():
    import sys
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def combinations_count(n, r, mod=10**9+7):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n-r)
        return fact[n] * factinv[r] * factinv[n-r] % mod
    
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

    A.sort()
    B = A[::-1]

    sum = 0
    for i in range(K-1, N):
        sum += combinations_count(i, K-1) * A[i] % MOD - combinations_count(i, K-1) * B[i] % MOD

    print(sum % MOD)


if __name__ == "__main__":
    resolve()