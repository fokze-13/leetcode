from math import ceil

n, m, k = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort(key = lambda x: ceil(x / 10) * 10 - x, reverse=True)
cnt = 0

for drink in b:
    if y * k >= drink:
        cnt += 1

        diff = ceil(drink / k)

        y -= diff
        x += diff * k - drink
    else:
        break

a.sort()
x += y * k

for dessert in a:
    if x >= dessert:
        cnt += 1

        x -= dessert
    else:
        break

print(cnt)
