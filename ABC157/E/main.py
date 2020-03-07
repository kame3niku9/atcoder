def resolve():
    N = int(input())
    S = list(input())
    Q = int(input())
    query = [input().split() for _ in range(Q)]

    for q in query:
        if q[0] == '1':
            idx = int(q[1]) - 1
            S[idx] = q[2]
        elif q[0] == '2':
            idx1 = int(q[1]) - 1
            idx2 = int(q[2]) - 1
            print(len(set(S[idx1:idx2+1])))

if __name__ == "__main__":
    resolve()