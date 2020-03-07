def resolve():

    A = [ list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]

    memo = [[0] * 3 for _ in range(3)]    

    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                memo[i][j] = 1

    for i in range(3):
        if memo[i][0] == 1 and memo[i][1] == 1 and memo[i][2] == 1:
            print("Yes")
            return
    
    for j in range(3):
        if memo[0][j] == 1 and memo[1][j] == 1 and memo[2][j] == 1:
            print("Yes")
            return

    if memo[0][0] == 1 and memo[1][1] == 1 and memo[2][2] == 1:
        print('Yes')
        return
    
    if memo[0][2] == 1 and memo[1][1] == 1 and memo[2][0] == 1:
        print("Yes")
        return
    
    print("No")


if __name__ == "__main__":
    resolve()