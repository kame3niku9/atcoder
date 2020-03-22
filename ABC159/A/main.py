import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def resolve():
    N, M = map(int, input().split())

    res = 0
    if N >= 2:
        res += combinations_count(N, 2)
    if M >= 2:
        res += combinations_count(M, 2)
    print(res)


if __name__ == "__main__":
    resolve()