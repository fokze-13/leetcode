from heapq import heappop_max, heappush_max

def sol(nums: list[int], k: int) -> list[int]:
    h = []
    res = []

    for i in range(k):
        t = (nums[i], i)
        heappush_max(h, t)
    res.append(h[0][0])

    for i in range(k, len(nums)):
        print(h, i)
        t = (nums[i], i)
        heappush_max(h, t)

        while h and h[0][1] + k <= i:
            heappop_max(h)
        res.append(h[0][0])

    return res


print(sol([9,10,9,-7,-4,-8,2,-6], 5))