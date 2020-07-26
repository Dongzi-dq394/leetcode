class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Something to learn from this problem:
        # 1. This is one typical question using monotonic queue
        # 2. Either increasing or decreasing
        res = []
        queue = []
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] <= n:
                queue.pop()
            queue.append(i)
            if queue[0] == i-k:
                queue.pop(0)
            if i >= k-1:
                res.append(nums[queue[0]])
        return res