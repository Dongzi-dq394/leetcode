class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # New Solution 1: Backtracking (40ms: 53.60%)
        # Can be improved by not using length (32ms: 87.28%)
        res = []
        def backtracking(sub_res, index):
            res.append(sub_res)
            for i in range(index, len(nums)):
                backtracking(sub_res+[nums[i]], i+1)
        backtracking([], 0)
        return res
        
        # New Solution 2: Array Flip (28ms: 96.10%)
        # Very smart!!
        res = [[]]
        for num in nums:
            length = len(res)
            for i in range(length):
                res.append(res[i]+[num])
        return res
        
        # New Solution 3: Bit Manupulation (36ms: 72.09%)
        # Can be improved by using bin() to (28ms: 96.10%)
        length = len(nums)
        res = []
        for i in range(1<<length):
            temp = []
            s = bin(i)
            s = '0'*(length+2-len(s)) + s[2:]
            for j in range(length):
                if s[j]=='1':
                    temp.append(nums[j])
            res.append(temp)
        return res