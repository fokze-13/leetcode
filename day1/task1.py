from collections import deque
from heapq import heapify_max, heappop_max

def sol(deck: list[int]) -> list[int]:
    heapify_max(deck)
    new = deque()

    new.appendleft(heappop_max(deck))
    new.appendleft(heappop_max(deck))

    while deck:
        a = new.pop()
        new.appendleft(a)
        new.appendleft(heappop_max(deck))

    return list(new)

print(sol([1, 1000]))
