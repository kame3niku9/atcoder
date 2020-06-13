import copy
from functools import lru_cache
def resolve():
    #N, K = map(int, input().split())
    #A = list(map(int, input().split()))

    N = 20000
    K = 20000
    A = [0] * N

    cut_mode = False
    
    if cut_mode and K + min(A) >= N:
        print(" ".join(map(str, [N]*N)))
        return

    @lru_cache(maxsize=100000)
    def func(i, a):
        A_tmp = [0] * len(A)
        #print(A_tmp[i:i+a+1])
        A_tmp[i:i+a+1] = [1]*(len(A_tmp[i:i+a+1]))

        #print(A_tmp[i-a:i+1])
        A_tmp[max(0, i-a):i+1] = [1]*(len(A_tmp[max(0, i-a):i+1]))
        
        #print(A_tmp)
        return A_tmp


    for k in range(K):
        #print("i", i)
        A_next = [0] * len(A)
        for i, a in enumerate(A):
            #print(i, a)
            A_tmp = func(i, a)
            #print("A_tmp", A_tmp)
            A_next = [x + y for (x, y) in zip(A_next, A_tmp)]
            #print("A_next", A_next)

        A = copy.deepcopy(A_next)
        #print("new A: ", A)

        print("k", k, "min(A)", min(A))

        if cut_mode and min(A) == N:
            break 

    print(" ".join(map(str, A_next)))

if __name__ == "__main__":
    resolve()