def resolve():
    n, k = map(int, input().split())
    cnt = 1
    while n >= k:
        n = n / k
        cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()