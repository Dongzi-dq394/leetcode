class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Something to learn from this problem:
        # 1. nums = nums[::-1] should be nums[:] = nums[::-1]
        # 2. The assignment should be nums[:]...
        
        # Solution 1: Exchange (112ms)
        k %= len(nums)
        if k!=0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        
        # Solution 2: Stack Operation (100ms)
        k = len(nums) - (k%len(nums))
        while k:
            nums.append(nums.pop(0))
            k -= 1
        
        # Solution 3: Reverse (128ms)
        k %= len(nums)
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        nums[:] = nums[::-1]