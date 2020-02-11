import math

def resolve():
    X = int(input())

    if X == 2:
        print(2)
        return

    if X % 2 == 0:
        i = X + 1
    else:
        i = X

    while True:
        isPrime = True
        for j in range(3, int(math.sqrt(i)), 2):
            if i % j == 0:
                isPrime = False
                break        
        if isPrime:
            print(i)
            return
        i += 2


if __name__ == "__main__":
    resolve()
