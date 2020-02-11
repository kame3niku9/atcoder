from functools import lru_cache

def resolve():
    import sys
    input = sys.stdin.readline
    
    H = int(input())

    @lru_cache(maxsize=None)
    def dfs(h):
        if h <= 1:
            return 1
        else:
            return 2 * dfs(h//2) + 1

    print(dfs(H))


if __name__ == "__main__":
    resolve()