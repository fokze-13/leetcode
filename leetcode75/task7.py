def sol(nums: list[int]) -> list[int]:
    out = [1] * len(nums)
    l = r = 1

    for i in range(0, len(nums) - 1):
        l *= nums[i]
        r *= nums[len(nums) - i - 1]

        out[i+1] *= l
        out[len(nums) - i - 2] *= r

    return out

print(sol([-1, 1, 0, -3, 3]))