class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        for i in range(length):
            if abs(nums[i]) <= length:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in range(length):
            if nums[i] >= 0:
                return i+1
        return length + 1