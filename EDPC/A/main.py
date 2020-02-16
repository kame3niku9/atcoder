def resolve():
    N = int(input())
    H = list(map(int, input().split()))

    dp = [0 for _ in range(N+5)]

    dp[0] = 0
    dp[1] = abs(H[1] - H[0])

    for i in range(1, N-1):
        dp[i+1] = min(dp[i-1] + abs(H[i+1] - H[i-1]), dp[i] + abs(H[i+1] - H[i]))

    print(dp[N-1])

if __name__ == "__main__":
    resolve()