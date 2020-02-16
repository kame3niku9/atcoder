# 1つづつ順に
# V << W なので、 dp[N][W]ではなく、 dp[N][V]で作成
def resolve():
    N, W = map(int, input().split())
    w_l = []
    v_l = []
    for _ in range(N):
        w, v = map(int, input().split())
        w_l.append(w)
        v_l.append(v)

    max_v = sum(v_l) + 1
    dp = [[10**10] * (max_v) for _ in range(N+1)] 
    dp[0][0] = 0

    for i in range(N):
        for j in range(max_v):
            #print(i, j)
            w = w_l[i]
            v = v_l[i]
            if j < v:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j - v] + w)
 
    res = 0
    for j in range(max_v):
        if dp[N][j] <= W:
            res = j

    print(res)

if __name__ == "__main__":
    resolve()