def resolve():
    N, M = map(int, input().split())

    L = [ [] for _ in range(N) ]

    for i in range(M):
        a, b = map(int, input().split())
        L[a-1].append(b-1)

    print(L)

    def dfs():
        st = 0
        




if __name__ == "__main__":
    resolve()