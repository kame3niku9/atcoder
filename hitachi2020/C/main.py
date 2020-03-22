from collections import deque
import numpy as np
def resolve():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N-1)]

    adj = [[] for _ in range(N)]
    for c in ab:
        a = c[0]-1
        b = c[1]-1
        adj[a].append(b)
        adj[b].append(a)

    three = [[] for _ in range(N)]
    pairs = set()

    # 距離3の頂点を探す
    INF = 9999999
    for i in range(N):
        reached = [INF] * N

        def bfs():
            que = deque([])
            que.append(i)
            reached[i] = 0

            while len(que) > 0:
                p = que.pop()
                #print(p)
                if reached[p] < 3:
                    for c in adj[p]:
                        if reached[c] == INF:
                            que.append(c)
                            reached[c] = reached[p] + 1
                            if reached[c] == 3:
                                three[i].append(c)
                                pairs.add((i, c))
        bfs()

    hub = list(map(len, three))
    x = np.argsort(hub)[::-1]

    def check(a, b):
        if (a + b) % 3 == 0 or (a * b) % 3 == 0:
            return True
        return False

    anser = list(range(1, N+1))
    good = [3] * (N//3)
    for i, g in enumerate(good):
        tmp = anser[x[i]]
        anser[x[i]] = g
        anser[g-1] = tmp

    print(' '.join(map(str, anser)))

if __name__ == "__main__":
    resolve()