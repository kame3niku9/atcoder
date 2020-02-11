import itertools

def resolve():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))
    l = list(itertools.permutations(range(1, N+1)))
    p_idx = l.index(P)
    q_idx = l.index(Q)
    print(abs(p_idx - q_idx))

if __name__ == "__main__":
    resolve()