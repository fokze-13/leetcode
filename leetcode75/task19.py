def sol(nums: list[int]) -> int:
    s = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = s - left_sum
        left_sum += nums[i]

        if left_sum == right_sum:
            return i

    return -1