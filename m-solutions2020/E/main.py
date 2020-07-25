def resolve():
    n = int(input())
    V = []  # 集落情報list
    for _ in range(n):
        #x, y, p = list(map(int, input().split()))
        V.append(list(map(int, input().split())))

    print(V)

    def distX(x, y, X):
        return abs(x - X)

    def distY(x, y, Y):
        return abs(y - Y)


    INF = 10**9

    def dist(v, RX, RY):
        v_x_min = INF
        v_y_min = INF
        for r in RX:
            d = abs(v[0] - r)
            if d < v_x_min:
                v_x_min = d
        for r in RY:
            d = abs(v[1] - r)
            if d < v_y_min:
                v_y_min = d
        v_min = min(v_x_min, v_y_min)
        
        return v_min

    def cost(v, dist):
        return v[2] * dist


    RX = [0]
    RY = [0]

    # 貪欲。前回の状態で最もcostが高いvに対して、xまたはyを追加する方策
    def calc(RX, RY, V):
        print("RX: ", RX)
        print("RY: ", RY)
        s = 0
        max_cost = 0
        max_cost_idx = 0
        for idx, v in enumerate(V):
            v_min = dist(v, RX, RY)
            cost_min = cost(v, v_min)
            print("v_min: ", v_min, "cost_min: ", cost_min)
            s += cost_min
            if cost_min > max_cost:
                max_cost = cost_min
                max_cost_idx = idx

        return s, max_cost_idx

    def selection(max_cost_idx, RX, RY):
        x = V[max_cost_idx][0]
        y = V[max_cost_idx][1]
        RX_ = RX[:]
        RY_ = RY[:]
        RX_.append(x)
        RY_.append(y)
        sx, ix = calc(RX_, RY, V)
        sy, iy = calc(RX, RY_, V)
        s_min = min(sx, sy)
        idx_min = ix if s_min == sx else iy
        return s_min, idx_min


    for k in range(n):
        if k == 0:
            s, max_cost_idx = calc(RX, RY, V)
            print(f"k:{k}, s: {s}")

        # 次のxまたはyを追加
        else:
            s_next, idx_next = selection(max_cost_idx, RX, RY)
            print(f"k:{k}, s: {s_next}")



if __name__ == "__main__":
    resolve()