class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = None
        for i, n in enumerate(nums):
            if n==0:
                if zero_pos == None:
                    zero_pos = i
            else:
                if zero_pos != None:
                    nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
                    zero_pos += 1