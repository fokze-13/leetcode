from heapq import heappush_max, heappop_max, heapify_max

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if m == 1:
        print(max(a))
        continue

    hp = a[:m - 1]
    heapify_max(hp)

    s = sum(hp)

    mx = m * a[m - 1] - s

    for k in range(m - 1, n - 1):
        if a[k] < hp[0]:
            s -= heappop_max(hp)
            s += a[k]
            heappush_max(hp, a[k])

        new = m * a[k + 1] - s
        mx = max(new, mx)

    print(mx)


