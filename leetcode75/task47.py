from heapq import heappush, heappop

def sol(costs: list[int], k: int, candidates: int) -> int:
    h = []
    l = 0
    r = len(costs) - 1

    for i in range(candidates):
        if l <= r:
            heappush(h, (costs[l], l))
            l += 1

        if r >= l:
            heappush(h, (costs[r], r))
            r -= 1

    total = 0

    for i in range(k):
        print(h)
        cost, index = heappop(h)
        print(cost, index, l, r)

        total += cost

        if index < l <= r:
            heappush(h, (costs[l], l))
            l += 1

        elif index > r >= l:
            heappush(h, (costs[r], r))
            r -= 1

    return total


print(sol([4866,4857,4378,4876,3594,4874,4717,4680,4813,4938,4156,4724], 9, 2))