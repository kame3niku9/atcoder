import math

def combinations_count(n):
    return math.floor(n*(n-1)/2)

def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    hist = [0] * 2*pow(10, 5)
    for a in A:
        hist[a-1] += 1

    all = 0
    for h in hist:
        if h >= 2:
            all += combinations_count(h)

    for a in A:
        h = hist[a-1]
        if h >= 2:
            diff = h-1
            print(all - diff)
        else:
            print(all)
    
if __name__ == "__main__":
    resolve()