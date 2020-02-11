def resolve():
    import sys
    input = sys.stdin.readline
    
    H, N = map(int, input().split())
    A = list(map(int, input().split()))

    S = sum(A)
    # print(S)

    if H - S <= 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    resolve()