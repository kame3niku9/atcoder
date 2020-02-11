import heapq

def resolve():
    N = int(input())
    P = list(map(int, input().split()))
    min_p = P[0]
    cnt = 0
    for i in range(0, N):    
        if P[i] <= min_p:
            cnt += 1
            min_p = P[i]
    print(cnt)


if __name__ == "__main__":
    resolve()