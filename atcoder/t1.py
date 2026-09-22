from heapq import heappop, heappush

n = int(input())

a = map(int, input().split())

s = []

for elem in a:
    heappush(s, elem)

    if len(s) > 3:
        heappop(s)

    if len(s) == 3:
        print(s[0])
