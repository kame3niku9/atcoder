import math
import numpy as np

def resolve():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if included(r1, c1, r2, c2):
        print(1)
        return

    # 候補1
    y_ = ((c1 + r1) + (c2 - r2)) / 2
    x_ = ((c1 + r1) - (c2 - r2)) / 2

    d_ = dist(r2, c2, x_, y_)

    # 候補2
    y__ = ((c2 + r2) + (c1 - r1)) / 2
    x__ = ((c2 + r2) - (c1 - r1)) / 2

    d__ = dist(r2, c2, x__, y__)

    if d_ <= d__:
        x = x_
        y = y_
    else:
        x = x__
        y = y__

    if included_dist(x, y, r2, c2):
        print(2)
        return

    if isinstance(x, int) and isinstance(y, int) and included(x, y, r2, c2):
        print(2)
        return

    if not isinstance(x, int) and not isinstance(y, int):
        print(3)
        return

    print(2)
    return

def included(x1, y1, x2, y2):
    if x1 + y1 == x2 + y2:
        return True
    if x1 - y1 == x2 - y2:
        return True
    if abs(x1 - x2) + abs(y1 - y2) <= 3:
        return True
    return False

def included_dist(x1, y1, x2, y2):
    if abs(x1 - x2) + abs(y1 - y2) <= 3:
        return True
    return False


def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 -y1)*(y2 - y1))




if __name__ == "__main__":
    resolve()