def sol(target: int, nums: list[int]) -> int:
    l = 0
    s = 0
    m = 0

    for r in range(len(nums)):
        s += nums[r]

        while s >= target:
            if m == 0:
                m = r - l + 1

            if r - l + 1 < m:
                m = r - l + 1

            s -= nums[l]
            l += 1

    return m

print(sol(7, [2,3,1,2,4,3]))