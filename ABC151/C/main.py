import numpy as np

def resolve():
    N, M = map(int, input().split())
    ACs = np.zeros(N)
    WAs = np.zeros(N)
    
    c_ac = 0
    c_wa = 0

    for i in range(M):
        p, s = input().split()
        if s == "WA":
            if ACs[int(p) - 1] == 0:
                WAs[int(p) - 1] += 1
        if s == "AC":
            ACs[int(p) - 1] += 1
            if ACs[int(p) - 1] == 1:
                c_ac += 1
                c_wa += WAs[int(p) - 1]

    print(int(c_ac), int(c_wa))
    

if __name__ == "__main__":
    resolve()