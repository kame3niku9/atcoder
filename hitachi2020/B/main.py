import numpy as np

def resolve():
    A, B, M = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    xyc = [list(map(int, input().split())) for _ in range(M)]
    #print(xyc)

    # 割引なしの状態での最小の組み合わせ
    i_no = np.argmin(al)
    j_no = np.argmin(bl)
    v_no= al[i_no] + bl[j_no]

    #print(i_no, j_no, v_no)

    v_min = v_no
    for c in xyc:
        v = al[c[0]-1] + bl[c[1]-1] - c[2]
        if v < v_min:
            v_min = v

    print(v_min)

if __name__ == "__main__":
    resolve()