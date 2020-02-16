from functools import lru_cache
from collections import defaultdict, deque


def resolve():
    N, M = map(int, input().split())
    es = [list(map(int, input().split())) for _ in range(M)]

    outs = defaultdict(list)
    ins = defaultdict(int)
    for v1, v2 in es:
        outs[v1].append(v2)
        ins[v2] += 1

    q = deque(v1 for v1 in range(M) if ins[v1] == 0)
    res = []
    while q:
        v1 = q.popleft()
        res.append(v1)
        for v2 in outs[v1]:
            ins[v2] -= 1
            if ins[v2] == 0:
                q.append(v2)

    print(res)


if __name__ == "__main__":
    resolve()