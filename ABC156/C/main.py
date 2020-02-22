from functools import lru_cache
def resolve():
    n = int(input())
    x = list(map(int, input().split()))

    x.sort()

    l = 0
    r = max(x)
    
    @lru_cache()
    def cost(p):
        s = 0
        for i in x:
            s += (i - p)**2
        return s

    while l + 1 < r:
        m = (l + r) // 2 
        l_s = cost(l)
        r_s = cost(r)
        if l_s > r_s:
            l = m
        else:
            r = m
    print(min(cost(l), cost(r)))


if __name__ == "__main__":
    resolve()