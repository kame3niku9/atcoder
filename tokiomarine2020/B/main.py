def resolve():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())

    dist = abs(A - B)
    dist_b = dist + W*T
    # if B <= A and (B - W*T) < (-10)**9:
    #     dist_b = abs(A - (-10)**9)

    # elif B > A and (B + W*T) > 10**9:
    #     dist_b = abs(A - 10**9)

    if V*T >= dist_b:
        print("YES")
    else:
        print("NO")




if __name__ == "__main__":
    resolve()