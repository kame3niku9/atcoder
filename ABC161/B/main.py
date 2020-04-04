def resolve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    all = sum(a)
    c = a[m-1]
    if c >= all / (4*m):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    resolve()