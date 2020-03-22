import numpy as np
def resolve():
    N = int(input())
    s = input()
    s = list(map(int, list(s)))
    a = np.array(s)
    for _ in range(N-1):
        a = np.abs(np.diff(a, n=1))
        print(a)
    print(a[0])

if __name__ == "__main__":
    resolve()