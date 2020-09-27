
def resolve():
    S = input()
    sub = "BW"
    cnt = 0
    sum = 0

    # 左端からのWと右端からのBは無関係のため除外
    st = 0
    end = 0
    for i, s in enumerate(S):
        if s == "B":
            break
        else:
            st += 1

    for i, s in enumerate(S[::-1]):
        #print(s)
        if s == "W":
            break
        else:
            end += 1

    #print(st, end)
    S = S[st:len(S)-end]
    #print(S)

    foundB = False
    for i, s in enumerate(S):
        if s == "B":
            cnt += 1
            foundB = True
        elif s == "W":
            sum += cnt
            foundB = False
        
        #print(s, cnt, sum)

    print(sum)


if __name__ == "__main__":
    resolve()