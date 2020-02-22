"""
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def combinations_count(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
"""

def resolve():
    n, a, b = map(int, input().split())

    all = 2 ** n

    mod = 10**9+7 #出力の制限
    N = n
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )

    def combinations_count(n, r, mod):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    all -= combinations_count(n, a, mod)
    all -= combinations_count(n, b, mod)

    if n==2 and a != b:
        print(0)
        return 

    print(all - 1)

if __name__ == "__main__":
    resolve()