def sol(nums: list[int], k: int) -> float:
    s = m = sum(nums[:k])

    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]

        if s > m:
            m = s

    return m / k
