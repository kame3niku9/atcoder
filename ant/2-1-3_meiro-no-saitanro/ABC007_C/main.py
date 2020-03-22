from collections import deque

def resolve():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [input() for _ in range(R)]
    print(maze)
    INF = 10**9
    memo = [[INF]*C for _ in range(R)]

    que = deque([(sy, sx)])
    print(que)

    def bfs():
        dx_dys = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(que):
            p = que.pop()
            print(p)
            # check goal
            if p == (gy, gx):
                return 
            
            # search candidates
            for dx_dy in dx_dys:
                ny = dx_dy[0]
                nx = dx_dy[1]
            
            

    bfs()

if __name__ == "__main__":
    resolve()