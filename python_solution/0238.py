class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        l_prod, r_prod = 1, 1
        l, r = 0, len(nums)-1
        while l<len(nums):
            res[l] *= l_prod
            res[r] *= r_prod
            l_prod *= nums[l]
            r_prod *= nums[r]
            l += 1
            r -= 1
        return res