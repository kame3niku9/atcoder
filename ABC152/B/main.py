def resolve():
    a, b = map(int, input().split())

    A = str(a)*b
    B = str(b)*a
    if A < B:
        print(A)
    else:
        print(B)


if __name__ == "__main__":
    resolve()