class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_far = nums[0]
        for i in range(len(nums)):
            if cur_far >= len(nums)-1:
                return True
            if i > cur_far:
                return False
            cur_far = max(cur_far, i+nums[i])