def resolve():
    N = int(input())
    d_list = [int(input()) for _ in range(N)]
    d_set = set(d_list)
    print(len(d_set))
    

if __name__ == "__main__":
    resolve()