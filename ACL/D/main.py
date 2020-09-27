import numpy as np
def resolve():
    n, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    nA = np.array(A)
    d = np.diff(nA, n=1)
    print(len(d[d <= k]))
    

if __name__ == "__main__":
    resolve()