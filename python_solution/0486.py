class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Solution 1: Memoization (28ms: 96.17%)
        # Similar to the Stone Game
        if len(nums)%2==0: return True
        memo = {}
        def helper(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if right==left:
                memo[(left, right)] = nums[left]
                return nums[left]
            temp = max(nums[left]-helper(left+1, right), nums[right]-helper(left, right-1))
            memo[(left, right)] = temp
            return temp
        res = helper(0, len(nums)-1)
        return True if res>=0 else False
        
        # Solution 2: DP (36ms: 71.98%)
        length = len(nums)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for j in range(length):
            for i in range(j, -1, -1):
                if i==j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return True if dp[0][length-1]>=0 else False