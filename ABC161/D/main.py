import numpy as np
def resolve():
    k = int(input())
    n = 20
    l = [[] for _ in range(n)]
    size = 0
    pre_size = 0

    for i in range(1, 10, 1):
        l[0].append(i)
    
    size += len(l[0])
    for j in range(n-1):
        if size >= k:
            break
        for var in l[j]:
            v = var % 10
            for a in range(v-1, v+2, 1):
                #print(a)
                if a >= 0 and a <= 9:
                    l[j+1].append(var*10 + a)
        size += len(l[j+1])
        pre_size += len(l[j])

    print(l[j][k - pre_size - 1])

if __name__ == "__main__":
    resolve()