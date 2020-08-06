class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Solution 1 from discussion: typical 0/1 knapsack problem (2336ms: 24.69%)
        sum_val = sum(nums)
        if sum_val%2==1:
            return False
        target = sum_val//2
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, 0, -1):
                if j>=nums[i]:
                    dp[j] = dp[j] | dp[j-nums[i]]
        return dp[target]
        
        # Solution 2 from discussion: Bit Manipulation (72ms: 80.43%)
        # So tricky!!!!!! wow!!!
        sum_val = 0
        bit = 1
        for num in nums:
            sum_val += num
            bit |= (bit<<num)
        return (sum_val%2==0) and ((bit>>(sum_val//2))%2==1)
        
        # Solution 3: Recursion from discussion (60ms: 83.85%)
        # Reverse sorting is the key point
        sum_val = sum(nums)
        if sum_val%2==1:
            return False
        nums.sort(reverse=True)
        def helper(target, index):
            if index>=len(nums):
                return False
            if nums[index]>target:
                return False
            if nums[index]==target:
                return True
            return helper(target-nums[index], index+1) or helper(target, index+1)
        return helper(sum_val//2, 0)