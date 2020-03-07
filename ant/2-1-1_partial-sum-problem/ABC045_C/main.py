def resolve():
    S = input()

    memo = []
    def dfs(s):
        if len(s) == len(S)-1:
            memo.append(s)
            return 
        dfs(s + "1")
        dfs(s + "0")

    dfs("")
    comb = []
    for c in memo:
        sub = []
        store = S[0]
        for i, flag in enumerate(c):
            if flag == "0":
                store += S[i+1]
            elif flag == "1":
                sub.append(store)
                store = S[i+1]
        sub.append(store)
        comb.append(sub)

    total = 0
    for c in comb:
        ilist = list(map(int, c))
        sum = 0
        for a in ilist:
            sum += a
        total += sum

    print(total)

if __name__ == "__main__":
    resolve()