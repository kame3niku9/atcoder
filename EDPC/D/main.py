# 1つづつ順に
def resolve():
    N, W = map(int, input().split())    
    w_v = [list(map(int, input().split())) for _ in range(N)]  # [N][0:weight, 1:value]

    dp = [[0] * (W+1) for _ in range(N+1)] 

    for i in range(N):
        for j in range(W+1):
            w = w_v[i][0]
            v = w_v[i][1]
            if j < w:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j - w] + v)
 
    print(dp[N][W])

# 遷移先を考えて移動。初期化は0
def resolve():
    N, W = map(int, input().split())    
    w_v = [list(map(int, input().split())) for _ in range(N)]  # [N][0:weight, 1:value]

    dp = [[0] * (W+1) for _ in range(N+1)] 

    for i in range(N):
        for j in range(W+1):
            w = w_v[i][0]
            v = w_v[i][1]
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j + w <= W:
                dp[i + 1][j + w] = max(dp[i][j] + v, dp[i + 1][j + w])
 
    print(dp[N][W])


if __name__ == "__main__":
    resolve()