import numpy as np
from collections import deque

def resolve():
    H, W = map(int, input().split())

    maze = []
    for i in range(H):
        maze.append(input())

    def bfs(st):

        INF = -1
        d = np.full((H, W), INF)

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        que = deque()
        que.append(st)
        d[st[1]][st[0]] = 0

        while len(que):
            p = que.popleft()

            for i in range(4):
                nx = p[0] + dx[i]
                ny = p[1] + dy[i]

                if nx >= 0 and nx < W and ny >= 0 and ny < H and maze[ny][nx] != "#" and d[ny][nx] == INF:
                    que.append([nx, ny])
                    d[ny][nx] = d[p[1]][p[0]] + 1

        cost = np.max(d)
        return cost

    max_cost = 0
    for y in range(H):
        for x in range(W):
            if maze[y][x] == '.':
                st = [x, y]
                cost = bfs(st)
                if cost > max_cost:
                    max_cost = cost 
    
    print(int(max_cost))

if __name__ == "__main__":
    resolve()