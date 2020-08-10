class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # New Solution: Adapted from KSum (812ms: 86.78%)
        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums)-1
            while l<r:
                temp = nums[l] + nums[r]
                if temp > target or (r<len(nums)-1 and nums[r]==nums[r+1]):
                    r -= 1
                elif temp < target or (l>0 and nums[l]==nums[l-1]):
                    l += 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        def KSum(nums, target, k):
            if len(nums) < k: return []
            if nums[0]*k > target or nums[-1]*k < target: return []
            if k==2: return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i==0 or nums[i]!=nums[i-1]:
                    for sub_res in KSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + sub_res)
            return res
        nums.sort()
        return KSum(nums, 0, 3)