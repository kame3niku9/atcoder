def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    flag = True
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                pass
            else:
                flag = False

    res = "APPROVED" if flag else "DENIED"
    print(res)

if __name__ == "__main__":
    resolve()