def resolve():
    N, Y = map(int, input().split())
    for i in range(N+1):
        for j in range(i, N+1):
            n_1man = i
            n_5sen = j - i
            n_1sen = N - (n_1man + n_5sen)

            total = 10000 * n_1man + 5000 * n_5sen + 1000 * n_1sen

            if total == Y:
                print("{} {} {}".format(n_1man, n_5sen, n_1sen))
                return
    print("-1 -1 -1")
    return

if __name__ == "__main__":
    resolve()
    


