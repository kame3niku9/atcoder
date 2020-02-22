def resolve():
    n, r = map(int, input().split())
    if n < 10:
        add = 100 * (10 - n)
        print(r + add)
    else:
        print(r)


if __name__ == "__main__":
    resolve()