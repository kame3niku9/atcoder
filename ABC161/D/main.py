import numpy as np
def resolve():
    k = int(input())
    n = 3234566667
    l = []
    i = 1
    while i < 13: 
        l.append(i)
        i += 1
        
    i = 21
    while i < n:
        a = list(map(int, str(i)))
        m = max(abs(np.diff(a)))
        if m <= 1:
            l.append(i)
            i += 1
        else:
            i += 8
    print(l)
    print(l[k-1])




if __name__ == "__main__":
    resolve()