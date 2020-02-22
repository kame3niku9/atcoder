def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    INF = 10**18 + 1

    # 「積がx未満となるペアの個数がK個未満」となる最大のxを求める
    l =  -INF  # OK
    r = INF  # NG

    # 二分探索 O(logN)
    def loop():
        total = 0
        for i in range(N):
            if A[i] < 0:
                l = -1
                r = N
                while l < r - 1:
                    center = (l + r) // 2
                    if A[center] * A[i] < x:
                        r = center
                    else:
                        l = center
                total += N - r
            else:
                l = -1
                r = N
                while l < r - 1:
                    center = (l + r) // 2
                    if A[center] * A[i] < x:
                        l = center
                    else:
                        r = center
                total += r
            if A[i] * A[i] < x:
                total -= 1
        total /= 2
        return total < K
        
    # 尺取り法 O(n)
    def loop2():


    while l < r - 1:
        x = (l + r) // 2
        if loop():
            l = x
        else:
            r = x
    print(l)


if __name__ == "__main__":
    resolve()