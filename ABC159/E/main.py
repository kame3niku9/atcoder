#da[i][j]:(0,0)~(i,j)の長方形の和
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    da[0][0] = a[0][0]
    print(da)
    for i in range(1,w):
        print(i)
        da[0][i] = da[0][i-1]+a[0][i]
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j]+cnt_w
    return da

#da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(p,q,x,y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y]-da[x][q-1]
    if q == 0:
        return da[x][y]-da[p-1][y]
    return da[x][y]-da[p-1][y]-da[x][q-1]+da[p-1][q-1]

def resolve():
    H, W, K = map(int, input().split())
    choco = [list(map(int, list(input()))) for _ in range(H)]

    print(choco)

    dp = [ [0] * W for _ in range(H)]

    dp[0][0] = 1 if choco[0][0] == "1" else 0
    
    for w in range(1, W):
        dp[0][w] = dp[0][w-1]+1 if choco[0][w] == "1" else dp[0][w-1]

    for h in range(1, H):
        dp[h][0] = dp[h-1][0]+1 if choco[h][0] == "1" else dp[h-1][0]

    for h in range(1, H):
        for w in range(1, W):
            prev = max(dp[h-1][w], dp[h][w-1])
            if choco[h][w] == '1':
                dp[h][w] = prev + 1
            else:
                dp[h][w] = prev 
    
    print(dp)


def resolve():
    H, W, K = map(int, input().split())
    choco = [input().split() for _ in range(H)]

    print(choco)
    print(choco[0][0])
    print(choco[0][0][0])

    da = da_generate(H, W, choco)
    print(da)


if __name__ == "__main__":
    resolve()