from math import log10

n, k = map(int, input().split())

res = n

digits = power = int(log10(n)) + 1

for i in range(k):
    if res % k == 0:
        print(i + 1)
        break

    res += n * (10**digits)
    digits += power
else:
    print(-1)
