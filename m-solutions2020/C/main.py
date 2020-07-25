def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(k, n):
        #print("i", i)
        j = i - k  # 比較対象
        #print("j", j)
        if A[i] > A[j]:
            print("Yes")
        else:
            print("No")




if __name__ == "__main__":
    resolve()