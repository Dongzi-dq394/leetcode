class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution 1: DP*3 (36ms: 52.27%)
        def helper(arr):
            dp = [0]*(len(arr)+1)
            dp[1] = arr[0]
            for i in range(1, len(arr)):
                dp[i+1] = max(dp[i], dp[i-1]+arr[i])
            return dp[-1]
        if not nums: return 0
        if len(nums)==1: return nums[0]
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))