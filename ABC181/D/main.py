def resolve():
    S = input()
    N = len(S)

    if N == 1:
        if int(S) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return

    elif N == 2:
        if int(S[0]+S[1]) % 8 == 0 or int(S[1]+S[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return

    elif N == 3:
        if judge_hachi(S[0], S[1], S[2]):
            print("Yes")
        else:
            print("No")
        return

    Stock = []
    i = 13
    while True:
        now = i*8
        if now >= 1000:
            break
        Stock.append(now)
        i += 1

    for num in Stock:
        SC = S[:]
        t = str(num)

        idx = SC.find(t[0])
        if idx == -1:
            continue
        SC = SC[:idx] + SC[idx+1:]

        idx = SC.find(t[1])
        if idx == -1:
            continue
        SC = SC[:idx] + SC[idx+1:]

        idx = SC.find(t[2])
        if idx == -1:
            continue
        SC = SC[:idx] + SC[idx+1:]


        print("Yes")
        return

    print("No")


def judge_hachi(a, b, c):
    if int(a+b+c) % 8 == 0 or int(a+c+b) % 8 == 0 or int(b+c+a) % 8 == 0 or int(b+a+c) % 8 == 0 or int(c+a+b) % 8 == 0 or int(c+b+a) % 8 == 0:
        return True
    return False


if __name__ == "__main__":
    resolve()