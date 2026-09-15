import heapq


def sol(nums1: list[int], nums2: list[int], k: int) -> int:
    s_pairs = sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True)

    curr_sum = 0
    heap = []
    ans = 0

    for pair in s_pairs:
        val = pair[0]
        print(pair, curr_sum, heap, ans)

        curr_sum += val
        heapq.heappush(heap, val)

        if len(heap) > k:
            m = heapq.heappop(heap)
            curr_sum -= m

        if len(heap) == k:
            ans = max(ans, curr_sum*pair[1])

    print(curr_sum, heap, ans)

    return ans



print(sol([1,3,3,2, 3, 2, 1,2,5,6,3,], [2,1,3,4,2,3,2,3,4,1], 3))

