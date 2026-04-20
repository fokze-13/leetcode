class NumArray:

    def __init__(self, nums: list[int]):
        self.psum = [0]
        for num in nums:
            self.psum.append(self.psum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right + 1] - self.psum[left]
