class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # There are two ways to solve this problem: Sort & Hash Table
        '''
        dic = {}
        for item in nums:
            if item in dic:
                return True
            dic[item] = True
        return False
        '''
        return len(set(nums)) != len(nums)