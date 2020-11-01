def resolve():
    N = int(input())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))

    #print(P)

    R = []

    for i in range(N):
        for j in range(i+1, N):
            # if i == j:
            #     continue
            R.append(calc_line(P[i][0], P[i][1], P[j][0], P[j][1]))

    #print(R)

    #print(len(R))
    #print(len(set(R)))
    #print(set(R))

    if len(R) != len(set(R)):
        print("Yes")
    else:
        print("No")

def calc_line(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 9999999
    b = y1 - a * x1
    return a, b

if __name__ == "__main__":
    #print(calc_line(0, 1, 2, 1))
    #print(calc_line(0, 1, 0, 0))
    resolve()