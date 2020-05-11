class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in dic:
                return [i, dic[left]]
            dic[nums[i]] = i