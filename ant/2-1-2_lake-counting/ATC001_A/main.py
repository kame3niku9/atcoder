import sys
sys.setrecursionlimit(10000000)

def resolve():
    H, W = map(int, input().split())
    M = [input() for _ in range(H)] # M[y][x]
    reached = [[False]*W for _ in range(H)]

    nds = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    goaled = False

    def dfs(y, x):
        nonlocal goaled
        if goaled:
            return
        if M[y][x] == "g":
            goaled = True
            return 
        if reached[y][x]:
            return

        reached[y][x] = True

        for nd in nds:
            ny = nd[0] + y
            nx = nd[1] + x

            if ny >= 0 and ny < H and nx >= 0 and nx < W and M[ny][nx] != "#":
                dfs(ny, nx)
        return

    # find s
    def find_s():
        for y in range(H):
            for x in range(W):
                if M[y][x] == 's':
                    return y, x
        return y, x

    y, x = find_s()
    dfs(y, x)

    if goaled:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    resolve()