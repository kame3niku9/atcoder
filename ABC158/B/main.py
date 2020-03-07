def resolve():
    N, A, B = map(int, input().split())

    d = N // (A + B)
    r = N % (A + B)

    print(d * A + min(r, A))


if __name__ == "__main__":
    resolve()