class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution 1: Use flag itself (176ms: 40%)
        if not nums: return 0
        length = len(nums)
        top = False
        for i in range(length):
            nums[i] += 1
        for item in nums:
            if abs(item) == length+1:
                top = True
            else:
                nums[abs(item)-1] = -abs(nums[abs(item)-1])
        if not top: return length
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        
        # Solution 2: Use Math (132ms: 95.20%)
        return len(nums)*(len(nums)+1)//2 - sum(nums)
        
        # Solution 3: Bit Manipulation (144ms: 70.51%)
        # All the index with len(nums) is [0,n]
        # If k is missing, then the res = 0 ^ k
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= i
            res ^= n
        return res