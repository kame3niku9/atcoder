def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    c = 0

    for i in range(0, N, 2):
        if a[i] % 2 != 0:
            c += 1

    print(c)


if __name__ == "__main__":
    resolve()