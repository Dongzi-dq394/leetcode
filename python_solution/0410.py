class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Solution 1 by myself: DP + Memo (TLE at the last case!!)
        '''
        memo = {}
        def helper(l, r, m):
            if (l, r, m) in memo:
                return memo[(l, r, m)]
            if m==1:
                memo[(l, r, m)] = sum(nums[l:r+1])
                return memo[(l, r, m)]
            if r-l+1==m:
                memo[(l, r, m)] = max(nums[l:r+1])
                return memo[(l, r, m)]
            res = float('Inf')
            pre_sum = 0
            for i in range(l, r+2-m):
                pre_sum += nums[i]
                temp = max(pre_sum, helper(i+1, r, m-1))
                res = min(res, temp)
            memo[(l, r, m)] = res
            return res
        return helper(0, len(nums)-1, m)
        '''
        # Solution from discussion: Binary Search (32ms: 86.80%)
        # Very Powerful!!!
        def helper(middle, m):
            count = 0
            pre_sum = 0
            for i in range(len(nums)):
                pre_sum += nums[i]
                if pre_sum>middle:
                    count += 1
                    pre_sum = nums[i]
            count += 1
            if count>m: return False
            else: return True
        l, r = max(nums), sum(nums)
        if m==1: return r
        if m==len(nums): return l
        while l<r:
            middle = (l+r)//2
            if helper(middle, m):
                r = middle
            else:
                l = middle+1
        return l