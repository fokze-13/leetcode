def sol(nums: list[int]) -> list[int]:
    n = len(nums)
    stack = [-n]
    res = [-1] * n

    for i in range(-n + 1, n):
        if nums[i] <= nums[stack[-1]]:
            if i < 0:
                stack.append(i)
        else:
            while stack and nums[i] > nums[pop_index := stack[-1]]:
                res[pop_index] = nums[i]
                stack.pop()
            if i < 0:
                stack.append(i)
    return res

print(sol([1,2,3,4,3]))