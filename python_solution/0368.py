class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Solution 1 by myself: Backtracking (TLE at the last test case!!)
        '''
        nums.sort()
        length = 0
        res = None
        def backtracking(sub_res, index):
            nonlocal length
            nonlocal res
            if index==len(nums):
                if len(sub_res)>length:
                    length = len(sub_res)
                    res = sub_res
                return
            if not sub_res:
                for i in range(index, len(nums)):
                    backtracking(sub_res+[nums[i]], i+1)
            else:
                for i in range(index, len(nums)):
                    if nums[i]%sub_res[-1]==0:
                        backtracking(sub_res+[nums[i]], i+1)
                if len(sub_res)>length:
                    length = len(sub_res)
                    res = sub_res
        backtracking([], 0)
        return res
        '''
        # Solution 2 by myself: DP (448ms: 53.41%)
        if not nums: return []
        nums.sort()
        length = 1
        index = 0
        dic = defaultdict(list)
        for i in range(len(nums)):
            flag = False
            for j in range(i):
                if nums[i]%nums[j]==0:
                    flag = True
                    if len(dic[nums[j]])+1>len(dic[nums[i]]):
                        dic[nums[i]] = dic[nums[j]]+[nums[i]]
                    if len(dic[nums[i]])>length:
                        length = len(dic[nums[i]])
                        index = i
            if not flag:
                dic[nums[i]].append(nums[i])
        return dic[nums[index]]