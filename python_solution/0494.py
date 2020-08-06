class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # Solution 1: DP from discussion (1024ms: 6.51%; 13.7M: 97.78%)
        sum_val = sum(nums)
        if sum_val<S or S<-sum_val: return 0
        dp = [0 for i in range(2*sum_val+1)]
        dp[sum_val] = 1
        for i in range(len(nums)):
            next_dp = [0 for i in range(2*sum_val+1)]
            for j in range(2*sum_val+1):
                if 0<=j+nums[i]<=2*sum_val:
                    next_dp[j] += dp[j+nums[i]]
                if 0<=j-nums[i]<=2*sum_val:
                    next_dp[j] += dp[j-nums[i]]
            dp = next_dp
        return dp[S+sum_val]
        
        # Solution 2: Another faster DP from discussion (124ms: 92.79%)
        # We can regard this problem as (positive/negative) set problem.
        # According to the problem, there should be Sum(P_set) - Sum(N_set) = S
        # --> Sum(P_set) + Sum(N_set) + Sum(P_set) - Sum(N_set) = S + Sum(nums)
        # --> 2 * Sum(P_set) = S + Sum(nums)
        # --> Sum(P_set) = (S + Sum(nums)) // 2
        # Now, use DP
        sum_val = sum(nums)
        if S>sum_val or S<-sum_val or (S+sum_val)%2==1: return 0
        target = (S+sum_val)//2
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
        return dp[target]