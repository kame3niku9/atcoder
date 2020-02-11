import math

def _resolve():
    import sys
    input = sys.stdin.readline
    
    H, N = map(int, input().split())
    v = []
    w = []
    for i in range(N):
        a, b = map(int, input().split())
        v.append(a)
        w.append(b)

    dp = [[0]*H for _ in range(N)]

    # initiate
    for i in range(H):
        dp[0][i] = w[0] * (math.ceil((i + 1) / v[0])) # 魔法1だけでHまで削るのに必要なコスト(MP)

    for i in range(1, N):
        for j in range(H):
            if j+1 < v[i]: 
                # 敵のHPが魔法iで与えるダメージより小さい場合、そのままの組み合わせか新しい魔法1回とで、コストの少ない方を選ぶ
                dp[i][j] = min(dp[i-1][j], w[i])
            else:
                # 大きい場合、そのままの組み合わせと、魔法iを取り込んだ組み合わせで、コストの少ない方を選ぶ
                dp[i][j] = min(dp[i-1][j], dp[i][j - v[i]] + w[i])

    print(dp[N-1][H-1])

def resolve():
    import sys
    input = sys.stdin.readline
    
    H, N = map(int, input().split())

    INF = 1001001001
    dp = [INF]*(H+1)

    dp[0] = 0
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(H):
            nj = min(j+a, H)
            dp[nj] = min(dp[nj], dp[j] + b)

    print(dp[H])


if __name__ == "__main__":
    resolve()