class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Solution 1: DP in O(n^n) (1224ms: 43.10%)
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
        # Solution 2: Binary Search from Solution (60ms: 79.06%)
        res = []
        for item in nums:
            index = bisect.bisect_left(res, item)
            if index >= len(res):
                res.append(item)
            else:
                res[index] = item
        return len(res)