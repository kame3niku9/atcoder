import math

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    A.sort()

    plus = []
    minus = []
    zeros = []
    for a in A:
        if a < 0:
            minus.append(a)
        elif a == 0:
            zeros.append(a)
        else:
            plus.append(a)

    def combinations_count(n, r):
        if n < r:
            return 0
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    minus_num = len(plus) * len(minus)
    zeros_num = sum([len(A) - i - 1 for i in range(len(zeros))])
    plus_num = combinations_count(len(plus), 2) + combinations_count(len(minus), 2)

    if K <= minus_num:
        m_idx = K // len(minus)
        p_idx = K % len(minus)
        minus.sort(reverse=True)
        plus.sort(reverse=True)
        res = minus[m_idx - 1] * plus[p_idx - 1]
    elif K <= zeros_num:
        res = 0
    else:
        store = []
        for i in range(len(plus)):
            for j in range(i+1, len(plus)):
                store.append(plus[i] * plus[j])
        for i in range(len(minus)):
            for j in range(i+1, len(minus)):
                store.append(minus[i] * minus[j])
        store.sort()
        idx = K - (minus_num + zeros_num)
        res = store[idx - 1]        

    print(res)


if __name__ == "__main__":
    resolve()