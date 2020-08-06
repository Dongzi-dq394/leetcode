class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Solution 1 by myself: flip (424ms: 50.50%, 21.6M)
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        return [i+1 for i, n in enumerate(nums) if n>0]
        
        # Solution 2 from discussion: Extra space (faster but using 24.8M)
        return list(set(range(1, len(nums)+1))-set(nums))