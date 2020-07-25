def resolve():
    r, g, b = map(int, input().split())
    k = int(input())

    c = 0
    # gがrより大きくなるまで2倍する
    while r >= g:
        g *= 2
        c += 1
    
    # bがgより大きくなるまで2倍する
    while g >= b:
        b *= 2
        c += 1

    if c <= k:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    resolve()