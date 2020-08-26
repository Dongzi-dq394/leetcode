class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def helper(l, r):
            if l+1==r:
                memo[(l, r)] = 0
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            temp = 0
            for m in range(l+1, r):
                temp = max(temp, nums[l]*nums[r]*nums[m]+helper(l,m)+helper(m,r))
            memo[(l, r)] = temp
            return temp
        return helper(0, len(nums)-1)