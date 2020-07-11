def resolve():
    L, R, d = map(int, input().split())
    c = 0
    for i in range(L, R+1):
        if i % d == 0:
            c += 1
    print(c)

if __name__ == "__main__":
    resolve()