dxys = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ts = None
xs = None
ys = None
N = None


def resolve():
    global ts
    global xs
    global ys
    global N
    N = int(input())
    ts = list()
    xs = list()
    ys = list()
    ts.append(0)
    xs.append(0)
    ys.append(0)
    for _ in range(N):
        t, x, y = map(int, input().split())
        ts.append(t)
        xs.append(x)
        ys.append(y)

    judge = dist_method()
    if judge:
        print("Yes")
    else:
        print("No")

def dfs(ct, cx, cy):
    if ct in ts:
        # try check
        i = ts.index(ct)
        if cx == xs[i] and cy == ys[i]:
            pass
        else:
            return False
        if i == len(ts) - 1:
            return True
        
    for dxy in dxys:
        nx = cx + dxy[0]
        ny = cy + dxy[1]
        if nx >= 0 and nx <= 100000 and ny >= 0 and ny <= 100000:
            if dfs(ct + 1, nx, ny):
                return True
    return False

def dist_method():
    for i in range(N):
        ct = ts[i]
        nt = ts[i+1]
        cx = xs[i]
        nx = xs[i+1]
        cy = ys[i]
        ny = ys[i+1]

        dt = nt - ct
        dist = abs(nx - cx) + abs(ny - cy)
        if dt < dist or dt % 2 != dist % 2:
            return False
    return True

if __name__ == "__main__":
    resolve()

