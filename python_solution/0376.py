class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Solution 1 by myself: DP (184ms: 21.84%)
        if not nums: return 0
        dp = [1]*len(nums)
        diff = [0]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]!=nums[j]:
                    if diff[j]==0:
                        if dp[j]+1>dp[i]:
                            diff[i] = -1 if nums[i]<nums[j] else 1
                            dp[i] = dp[j]+1
                    elif diff[j]==-1:
                        if nums[i]>nums[j]:
                            if dp[j]+1>dp[i]:
                                diff[i] = 1
                                dp[i] = dp[j]+1
                    else:
                        if nums[i]<nums[j]:
                            if dp[j]+1>dp[i]:
                                diff[i] = -1
                                dp[i] = dp[j]+1
        return max(dp)
        
        # Solution 2: Greedy (40ms: 56.32%)
        if len(nums)<2: return len(nums)
        pre_diff = nums[1]-nums[0]
        res = 2 if pre_diff!=0 else 1
        for i in range(2, len(nums)):
            cur_diff = nums[i]-nums[i-1]
            if (cur_diff>0 and pre_diff<=0) or (cur_diff<0 and pre_diff>=0):
                res += 1
                pre_diff = cur_diff
        return res
        
        # Solution 3: DP from discussion (36ms: 71.74%)
        if not nums: return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                up = down+1
            elif nums[i]<nums[i-1]:
                down = up+1
            else:
                continue
        return max(down, up)