def resolve():
    N = int(input())


    def f(x,y,z):
        return x*x + y*y + z*z + x*y + y*z + z*x

    hist = [0] * 100*100*100

    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                n = f(x,y,z)
                hist[n] += 1

    for i in range(1, N+1):
        print(hist[i])


if __name__ == "__main__":
    resolve()