def resolve():
    x = int(input())
    n500, x = divmod(x, 500)
    n5 = x // 5
    res = n500 * 1000 + n5 * 5
    print(res)


if __name__ == "__main__":
    resolve()