# dpに文字列を格納 (TLE)
def resolve():
    s = input()
    t = input()

    dp = [[""] * (len(t)+1) for _ in range(len(s)+1)]
    
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + s[i]
            else:
                if len(dp[i][j+1]) >= len(dp[i+1][j]):
                    dp[i+1][j+1] = dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i+1][j]

    print(dp[len(s)][len(t)])

def resolve():
    s = input()
    t = input()

    dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
    
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # 後ろから探索
    # s[i-1]が、LCSに含まれるかどうか判定
    # dp[i][j]とdp[i-1][j]またはdp[i][j-1]が一致(変化なし)の場合、s[i-1]はLCSに含まれない
    res = ""
    i = len(dp) - 1
    j = len(dp[0]) - 1
    while i != 0 and j != 0:
        if dp[i][j] == dp[i - 1][j]: 
            i -= 1 
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res = s[i-1] + res
            i -= 1
            j -= 1

    print(res)

if __name__ == "__main__":
    resolve()