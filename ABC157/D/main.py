from functools import lru_cache
def resolve():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    # 幅優先探索 + cacheで、各ノードから到達可能な全てのnodeを取得する ( by 友達リスト)
    @lru_cache()
    def bfs(n):
        pass

    # 到達可能な全てのnodeの内、本人から直接繋がっていないnodeかつ、ブロックリストに入っていないnode = 友達候補





if __name__ == "__main__":
    resolve()