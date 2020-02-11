cost = 0
X = None
def resolve():
    N = int(input())
    global X
    X = list(map(int, input().split()))

    MOD = 1000000007

    R = list(range(N))

    total = dfs(0, R, 0)
    print("total", total)


def dfs(idx, r, cost):
    #print(X)
    print(idx)
    #print(r)
    if len(r) == 1:
        print("X[r[0]]", X[r[0]])
        print("X[idx]", X[idx])
        return abs(X[r[0]] - X[idx])

    for i in range(len(r)):
        cost += dfs(r[i], list(set(r) - set([r[i]])), cost)
    return cost


if __name__ == "__main__":
    resolve()