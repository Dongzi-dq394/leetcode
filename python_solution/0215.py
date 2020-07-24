class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        s_start, l_start = 1, len(nums)-1
        while True:
            while s_start <= l_start and nums[l_start] >= pivot:
                l_start -= 1
            while s_start <= l_start and nums[s_start] <= pivot:
                s_start += 1
            if s_start <= l_start:
                nums[s_start], nums[l_start] = nums[l_start], nums[s_start]
            else:
                break
        if len(nums)-1-l_start == k-1:
            return pivot
        elif len(nums)-1-l_start > k-1:
            return self.findKthLargest(nums[l_start+1:], k)
        else:
            return self.findKthLargest(nums[1:s_start], k-len(nums)+l_start)