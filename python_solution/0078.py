class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1: Backtracking
        def backtrack(target_length, index, cur):
            if len(cur) == target_length:
                res.append(cur)
                return
            else:
                for i in range(index, length):
                    backtrack(target_length, i+1, cur+[nums[i]])
        res = []
        length = len(nums)
        for i in range(length+1):
            backtrack(i, 0, [])
        return res
    
        # Solution 2: Recursion
        if not nums: return [[]]
        former = self.subsets(nums[1:])
        length = len(former)
        for i in range(length):
            former.append(former[i]+[nums[0]])
        return former