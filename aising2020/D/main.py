from functools import lru_cache

def resolve():
    #N = int(input())
    #X_ori = list(input())  # string ["0", "1", "1"]

    N = 20000
    X_ori = ["0"]*N

    def popcount_(s):
        return s.count("1")

    @lru_cache(maxsize=1000000)
    def popcount(x):
        x_bin = bin(x)[2:]
        n = popcount_(x_bin)
        return n

    @lru_cache(maxsize=1000000)
    def func(n):
        if n == 0:
            return 0
        c = 0
        while True:
            c += 1
            n_c = popcount(n)
            n = n % n_c
            if n == 0:
                break

        return c

    X_ini = "".join(X_ori)
    n_ini = popcount_(X_ini)

    for i in range(len(X_ori)):
        X = X_ori[:]
        X[i] = "1" if X[i] == "0" else "0"
        n_st = n_ini + 1 if X[i] == "1" else n_ini - 1
        X = "".join(X)
        X_dec = int(X, 2)
        X_st = X_dec % n_st
        #c = func(X_st) + 1
        c = 0
        print(c)
    

if __name__ == "__main__":
    resolve()