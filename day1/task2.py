def sol(nums1: list[int], nums2: list[int]):
    h = {}

    for j in range(len(nums2)):
        h[nums2[j]] = -1
        for t in range(j, len(nums2)):
            if nums2[t] > nums2[j]:
                h[nums2[j]] = nums2[t]
                break

    return [h[i] for i in nums1]

print(sol([2, 4], [1, 2, 3, 4]))
