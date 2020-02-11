import numpy as np
def resolve():
    N = int(input())

    freq = np.zeros((10, 10))
    for i in range(1, N+1):
        s = str(i)
        head = int(s[0])
        tail = int(s[-1])
        freq[head][tail] += 1
        
    ans = 0
    for i in range(1, N+1):
        s = str(i)
        head = int(s[0])
        tail = int(s[-1])
        ans += freq[tail][head]      

    print(int(ans))
    

if __name__ == "__main__":
    resolve()