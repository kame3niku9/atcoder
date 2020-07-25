from collections import deque

def resolve():
    T = int(input())  # 以内
    N = int(input())  # たこ焼きの数
    A = deque(list(map(int, input().split())))  # たこ焼きの焼き上がる時間
    M = int(input())  # お客さんの数
    B = deque(list(map(int, input().split())))  # お客さんのやってくる時間

    for _ in range(M):
        b = B.popleft()
        #print("b", b)
        while True:
            if len(A) == 0:
                print("no")
                return
            a = A.popleft()
            #print("a", a)
            # お客さんに提供するたこ焼きがこれで良いか判定
            if a > b:
                # お客さんを待たせてしまったのでNG
                print("no")
                return
            elif b - a <= T:
                # たこ焼きaで良い
                break

    print("yes")


if __name__ == "__main__":
    resolve()