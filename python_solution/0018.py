class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            # Version 1: Hash Table (212ms: 62.79%)
            res = []
            ele = set() # Set is better than dict
            for i in range(len(nums)):
                #if i==0 or nums[i]!=nums[i-1]: # This one is wrong!!!
                if len(res)==0 or res[-1][0]!=nums[i]:
                    if target-nums[i] in ele:
                        res.append([nums[i], target-nums[i]])
                    ele.add(nums[i])
            return res
            
            # Version 2: Two Pointers (180ms: 65.83%)
            res = []
            l, r = 0, len(nums)-1
            while l<r:
                temp = nums[l]+nums[r]
                if temp<target or (l>0 and nums[l]==nums[l-1]):
                    l += 1
                elif temp>target or (r<len(nums)-1 and nums[r]==nums[r+1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        
        def KSum(nums, target, k):
            if len(nums)<k: return []
            if k==2: return twoSum(nums, target)
            res = []
            if nums[0]*k>target or nums[-1]*k<target: return res
            for i in range(len(nums)):
                if i==0 or nums[i]!=nums[i-1]:
                    for subres in KSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]]+subres)
            return res
        
        # Must be sorted
        nums.sort()
        return KSum(nums, target, 4)