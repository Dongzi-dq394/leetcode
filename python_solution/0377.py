class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Solution 1 by myself: Backtracking (TLE!!!)
        '''
        res = 0
        def helper(m, n):
            res = 1
            for i in range(m, m-n, -1):
                res *= i
            for i in range(1, n+1):
                res //= i
            return res
        def calculate(arr):
            temp = []
            start = 0
            res = 1
            i = 1
            while i<len(arr):
                if arr[i]!=arr[i-1]:
                    temp.append(i-start)
                    start = i
                i += 1
            temp.append(i-start)
            start = len(arr)
            for i in range(len(temp)):
                res *= helper(start, temp[i])
                start -= temp[i]
            return res
        def backtracking(sub_res, remain, index):
            if remain==0:
                nonlocal res
                res += calculate(sub_res)
                return
            if index==len(nums) or remain<0:
                return
            for i in range(index, len(nums)):
                backtracking(sub_res+[nums[i]], remain-nums[i], i)
        backtracking([], target, 0)
        return res
        '''
        # Solution from discussion: DP + memo (36ms: 97.35%)
        memo = {}
        def helper(n):
            if n==0:
                memo[n] = 1
                return 1
            if n in memo:
                return memo[n]
            res = 0
            for i in range(len(nums)):
                if n>=nums[i]:
                    res += helper(n-nums[i])
            memo[n] = res
            return res
        return helper(target)