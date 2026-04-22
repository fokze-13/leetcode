def sol(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    h = {num: 1 for num in nums1}

    for num in nums2:
        if h.get(num) is None:
            h[num] = -1
        elif h.get(num) == 1:
            h[num] -= 1

    first = []
    second = []

    for key in h:
        if h[key] == 1:
            first.append(key)
        elif h[key] == -1:
            second.append(key)

    return [first, second]

print(sol([1, 2, 3], [2, 4, 6]))