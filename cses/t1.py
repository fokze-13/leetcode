from itertools import accumulate

n, k = map(int, input().split())

a = list(map(int, input().split()))

ps = [0] + list(accumulate(a))

for _ in range(k):
    l, r = map(int, input().split())

    print(ps[r] - ps[l - 1])

