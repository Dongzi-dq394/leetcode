class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use DP
        dp = nums[0]
        res = dp
        for i in range(1, len(nums)):
            dp = max(dp+nums[i], nums[i])
            res = max(res, dp)
        return res
        
        # Use Divide and Conquer
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2:
            if nums[0]>=0 and nums[1]>=0: return nums[0]+nums[1]
            else: return max(nums[0], nums[1])
        
        middle = len(nums) // 2
        l_start, r_start = middle-1, middle+1
        l_sum = r_sum = nums[middle]
        l_max = r_max = nums[middle]
        while l_start>=0:
            l_sum += nums[l_start]
            if l_sum > l_max:
                l_max = l_sum
            l_start -= 1
        while r_start <= length-1:
            r_sum += nums[r_start]
            if r_sum > r_max:
                r_max = r_sum
            r_start += 1
        continue_max = l_max + r_max - nums[middle]
        return max(continue_max, self.maxSubArray(nums[:middle]), self.maxSubArray(nums[middle+1:]))