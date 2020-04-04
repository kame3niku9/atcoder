def resolve():
    n, k = map(int, input().split())
    if n > k:
        m = n % k
        a = abs(m - k)
        b = abs(a - k)
        print(min(a, b))
        return
    else:
        a = abs(n - k)
        b = abs(a - k)
        print(min(a, b))



if __name__ == "__main__":
    resolve()