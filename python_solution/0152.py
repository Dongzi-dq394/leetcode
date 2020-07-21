class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        Min = [0] * len(nums)
        Max = [0] * len(nums)
        Min[0] = Max[0] = nums[0]
        for i in range(1, len(nums)):
            Min[i] = min(nums[i]*Min[i-1], nums[i]*Max[i-1], nums[i])
            Max[i] = max(nums[i]*Min[i-1], nums[i]*Max[i-1], nums[i])
        return max(Max)