import numpy as np

def resolve():
    S = []
    T = []
    N = int(input())
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    X = input()

    idx = S.index(X)
    cumsum = np.cumsum(np.array(T))
    time = cumsum[-1] - cumsum[idx]
    print(time)

if __name__ == "__main__":
    resolve()

