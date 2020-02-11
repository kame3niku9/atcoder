def resolve():
    N_500 = int(input())
    N_100 = int(input())
    N_50 = int(input())
    dist = int(input())
    ans = 0

    for i in range(N_500 + 1):
        for j in range(N_100 + 1):
            for k in range(N_50 + 1):
                if i * 500 + j * 100 + k * 50 == dist:
                    ans += 1

    print(ans)

