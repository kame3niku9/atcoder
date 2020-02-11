def resolve():
    import sys
    input = sys.stdin.readline
    
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)
    res = H[K:]
    
    S = sum(res)
    print(S)

if __name__ == "__main__":
    resolve()