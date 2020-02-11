from functools import reduce
from operator import add

def resolve():
    sum = 0
    N, A, B = map(int, input().split())
    for i in range(1, N+1):
        _sum = calc_sum(i) 
        if _sum >= A and _sum <= B:
            sum += i
    print(sum)

def calc_sum(number):
    l = list(map(int, str(number)))
    return reduce(add, l)


if __name__ == "__main__":
    resolve()