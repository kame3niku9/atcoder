def resolve():
    N, M = map(int, input().split())
    SC = [list(map(int, input().split())) for _ in range(M)]

    res = [0] * N
    called = [0] * N

    for sc in SC:
        s = sc[0] - 1
        c = sc[1]
        # 同じ桁を指定しながら、別の数値を指定した場合
        if called[s] == 1 and res[s] != c:
            print(-1)
            return
        
        res[s] = c
        called[s] = 1

    # 先頭が0となる場合
    if N != 1 and res[0] == 0:
        if called[0] == 1:
            print(-1)
            return
        else:
            res[0] = 1

    print(''.join(map(str, res)))



if __name__ == "__main__":
    resolve()