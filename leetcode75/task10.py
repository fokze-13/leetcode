nums = [4,2,4,0,0,3,0,5,1,0]

i = 0
j = 1

while i < len(nums) and j < len(nums):
    if nums[i] == 0:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    else:
        if nums[i] != 0:
            i += 1
    j += 1

print(nums)

