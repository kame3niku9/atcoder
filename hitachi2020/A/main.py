def resolve():
    S = input()
    for i in range(0, len(S), 2):
        if S[i:i+2] != 'hi':
            print("No")
            return

    print("Yes")
        

if __name__ == "__main__":
    resolve()