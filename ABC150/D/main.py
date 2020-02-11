import fractions
from functools import reduce


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def calc(x, a):
    p = x / a - 0.5
    if p == int(p):
        return True
    else:
        return False

def resolve():
    N, M = map(int, input().split())
    A = list(set(map(int, input().split())))
    A_sorted = sorted(A, reverse=True)

    lcm = lcm_list(A)
    #print(lcm)
    if lcm//2 > M:
        print(0)
        return

    max_a = A_sorted[0]
    find_x = 0
    for p in range(0, lcm//2):
        x = max_a * (p + 0.5)
        # print("x", x)
        find_flg = True
        for a in A_sorted[1:]:
            if not calc(x, a):
                find_flg = False
                # print("not found")
                break
        if find_flg:
            find_x = x
            break
            
    # print("find_x", x)
    if find_x == 0:
        print(0)
        return
    res = M - find_x
    count_c = int(res // lcm) + 1

    print(count_c)


if __name__ == "__main__":
    resolve()