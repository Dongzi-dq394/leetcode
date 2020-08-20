class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Old Solution: Use quick sort (3636ms: 5.03%)
        pivot = nums[0]
        l, r = 1, len(nums)-1
        while True:
            while l<=r and nums[l]<pivot:
                l += 1
            while l<=r and nums[r]>=pivot:
                r -= 1
            if l>r:
                break
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if len(nums)-r==k:
            return pivot
        elif len(nums)-r>k:
            return self.findKthLargest(nums[r+1:], k)
        else:
            return self.findKthLargest(nums[1:l], k-len(nums)+r)
        
        # New Solution 1: Sort (92ms: 43.55%)
        return sorted(nums, reverse=True)[k-1]
        
        # New Solution 2: min-Heap from Python (68ms: 78.38%)
        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return heappop(nums)