class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def helper(arr, k):
            ans = -float('Inf')
            pre_sum = 0
            dic = [0]
            for item in arr:
                pre_sum += item
                index = bisect.bisect_left(dic, pre_sum-k)
                if index<len(dic):
                    ans = max(ans, pre_sum-dic[index])
                index = bisect.bisect_left(dic, pre_sum)
                dic.insert(index, pre_sum)
            return ans
        res = -float('Inf')
        height, width = len(matrix), len(matrix[0])
        for i in range(width):
            dp = [0]*height
            for j in range(i, width):
                for x in range(height):
                    dp[x] += matrix[x][j]
                res = max(res, helper(dp, k))
        return res