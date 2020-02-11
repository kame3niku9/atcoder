def resolve():
    A, B, K = map(int, input().split())
    A_res = A - K
    if A_res >= 0:
        print(A_res, B)
        return
    
    B_res = B + A_res
    if B_res >= 0:
        print(0, B_res)
        return 

    print(0, 0)


if __name__ == "__main__":
    resolve()