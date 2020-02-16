
from collections import defaultdict
def resolve():
    N = int(input())
    S = [input() for _ in range(N)]
    
    res = defaultdict(int)

    for s in S:
        res[s] += 1

    max_v = max(res.values())
    max_k_list = [kv[0] for kv in res.items() if kv[1] == max_v]

    max_k_list.sort()
    for k in max_k_list:
        print(k)


if __name__ == "__main__":
    resolve()