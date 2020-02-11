n = 4
a = [1,2,4,7]
k = 2

# 深さ優先探索
def dfs(i, sum):
    print(i, sum)
    if sum > k:
        print("枝刈り")
        return False
    if i == n:
        print("sum: {}".format(sum))
        print("k: {}".format(k))
        print(sum==k)
        return sum == k
    if dfs(i+1, sum):  # 追加しない場合
        return True
    if dfs(i+1, sum + a[i]):  # 追加する場合
        return True
    return False

print(dfs(0, 0))
