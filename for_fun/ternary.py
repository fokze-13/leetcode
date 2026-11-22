n, p = map(int, input().split())
a = [(int(inp), i) for i, inp in enumerate(input().split())]

a.sort()

mn_i = 0
mn_j = 1

def f_plus(d: int, v: int) -> float:
    return d / v - p

for i in range(n):
    cands = set()
    dist = a[i]

    l = -1
    r = n - 1

    mid = (l + r) // 2

    while r - l > 1:
        if -f_plus(dist[0], a[mid][0]) <= 0:
            l = mid

        else:
            r = mid

        mid = (l + r) // 2

    cands |= {max(l, 0), max(0, l - 1), min(n - 1, l + 1), max(0, l - 2), min(n - 1, l + 2)}

    if i in cands:
        cands.remove(i)

    for cand in cands:
        if abs(f_plus(dist[0], a[cand][0])) < abs(f_plus(a[mn_i][0], a[mn_j][0])):
            mn_i = i
            mn_j = cand

print(a[mn_i][1] + 1, a[mn_j][1] + 1)