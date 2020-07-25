def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    c = 1000
    s = 0

    for i in range(0, n-1):
        j = i + 1  # 比較対象(翌日)
        diff = A[j] - A[i]
        # 次にup 今持っている現金を全て株にする
        if diff > 0:
            s += c // A[i]
            c = c % A[i]
        # 次にdown 今持っている株を全て現金にする
        elif diff < 0:
            c += s * A[i]
            s = 0
        #print(i, s, c)

    # 最後に株を全て現金に戻す
    c += s * A[n-1]

    print(c)


if __name__ == "__main__":
    resolve()