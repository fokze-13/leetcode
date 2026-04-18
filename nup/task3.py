from heapq import heappop, heappush

n, m, d = map(int, input().split())
t = list(map(int, input().split()))

c = 0
visitors = []

for visitor in t:
    if len(visitors) < n:
        heappush(visitors, visitor)
        c += 1
    else:
        if visitors[0] + d <= visitor:
            heappop(visitors)
            heappush(visitors, visitor)
            c += 1

print(c)