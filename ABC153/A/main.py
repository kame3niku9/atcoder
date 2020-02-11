import math
def resolve():
    import sys
    input = sys.stdin.readline
    
    H, A = map(int, input().split())

    print(math.ceil(H / A))
    

if __name__ == "__main__":
    resolve()