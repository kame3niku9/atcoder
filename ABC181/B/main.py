def resolve():
    N = int(input())
    C = [0]
    for i in range(1, 10**6+1):
        C.append(C[i - 1] + i)

    sum = 0
    for _ in range(N):
        a, b = map(int, input().split())
        sum += C[b] - C[a-1]

    print(sum)

if __name__ == "__main__":
    resolve()