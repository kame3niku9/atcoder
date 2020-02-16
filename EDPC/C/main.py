def resolve():
    N = int(input())
    dp = [[0] * 3 for _ in range(N)]
    table = [list(map(int, input().split())) for _ in range(N)]

    dp[0][0] = table[0][0] # a0
    dp[0][1] = table[0][1] # b0
    dp[0][2] = table[0][2] # c0

    for i in range(1, N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + table[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + table[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + table[i][2]

    res = max(dp[N-1])
    print(res)    

if __name__ == "__main__":
    resolve()