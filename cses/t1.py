n = int(input())
a = list(map(int, input().split()))

d = {}

l = 0

cnt = 0

for i in range(n):
    if d.get(a[i]) is not None:
        l = max(l, d[a[i]] + 1)

    d[a[i]] = i

    cnt += i - l + 1

print(cnt)
