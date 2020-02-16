def resolve():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    dp = [0] * N

    for i in range(1, N):
        s = max(0, i-K)
        dp[i] = min([c + abs(h - H[i]) for c, h in zip(dp[s:i], H[s:i])] )

    print(dp[N-1])

if __name__ == "__main__":
    resolve()
