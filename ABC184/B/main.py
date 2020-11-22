def resolve():
    N, X = map(int, input().split())
    S = input()

    for i, s in enumerate(S):
        if s == "x" and X != 0:
            X -= 1
        elif s == "o":
            X += 1


    print(X)

if __name__ == "__main__":
    resolve()