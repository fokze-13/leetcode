from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

l = 0
r = 0

mx = 0

while r < n:
    if d[a[r]] > 0:
        d[a[l]] -= 1

        l += 1
    else:
        d[a[r]] += 1

        mx = max(mx, r - l + 1)

        r += 1

print(mx)
