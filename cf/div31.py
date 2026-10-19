from math import comb

t = int(input())

def func(x: int) -> int:
    res = 0
    while x > 0:
        res += (x % 10) ** 2
        x //= 10
    return res

for _ in range(t):
    n = int(input())
    a = map(int, input().split())

    d = {1: 0}

    for num in a:
        for i in range(50):
            num = func(num)

        d[num] = d.get(num, 0) + 1

    res = 0

    for v in d.values():
        res += comb(v, 2)

    print(res)
