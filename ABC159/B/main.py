import math
def resolve():
    S = input()
    N = len(S)
    pre = S[0:math.floor((N-1)/2)]
    post = S[math.floor((N+3)/2 - 1):]
    if S == S[::-1] and pre == pre[::-1] and post == post[::-1]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    resolve()