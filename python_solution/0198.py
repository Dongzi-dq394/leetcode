class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = [0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return nums[-1]