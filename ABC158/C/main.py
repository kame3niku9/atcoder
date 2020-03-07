import math
def resolve():
    A, B = map(int, input().split())

    for x in range(1, 100*100):
        a = math.floor(x * 0.08)
        b = math.floor(x * 0.1)
        if a == A and b == B:
            print(x)
            return
    
    print(-1)
    return

if __name__ == "__main__":
    resolve()