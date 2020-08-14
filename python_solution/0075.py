class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # New Solution: Two Pointers (32ms: 81.42%)
        if not nums: return
        start = 0
        l, r = 0, len(nums)-1
        # All the number in nums[:start] is 0/1 (or empty) and sorted in '0...1...'
        # All the number in nums[r+1:] is 2 (or empty)
        # So, when start>r, the nums has already sorted --> exit the while-loop
        while start<=r:
            if nums[start]==0:
                nums[l], nums[start] = nums[start], nums[l]
                l += 1
                start += 1
            elif nums[start]==2:
                nums[r], nums[start] = nums[start], nums[r]
                r -= 1
                # start should be same here because we need to know whether the
                # new number exchanged from the tail is still 2 or not.
            else:
                start += 1