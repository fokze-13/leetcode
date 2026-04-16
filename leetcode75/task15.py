nums = [0]
k = 0

zeros = 0
m = 0

i = 0
j = 0

while j < len(nums):
    if nums[j] == 0:
        zeros += 1

    while zeros > k:
        if nums[i] == 0:
            zeros -= 1
        i += 1

    j += 1

    if j - i > m:
        m = j - i

print(m)
