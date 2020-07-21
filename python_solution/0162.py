class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(l, r):
            if l==r: return l
            if l+1==r: return l if nums[l] > nums[r] else r
            middle = (l + r) // 2
            if nums[middle]>nums[middle-1] and nums[middle]>nums[middle+1]:
                return middle
            elif nums[middle] < nums[middle-1]:
                return helper(l, middle)
            else:
                return helper(middle, r)
        return helper(0, len(nums)-1)