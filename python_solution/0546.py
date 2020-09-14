class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # Solution by myself: Memoization (TLE!!)
        '''
        memo = {}
        def helper(arr):
            key = str(arr)
            if key in memo:
                return memo[key]
            if not arr:
                return 0
            start = 0
            res = 0
            while start<len(arr):
                end = len(arr)
                for i in range(start+1, len(arr)):
                    if arr[i]!=arr[start]:
                        end = i
                        break
                res = max(res, (end-start)**2+helper(arr[:start]+arr[end:]))
                start = end
            memo[key] = res
            return res
        return helper(boxes)
        '''
        # Solution from discussion: 3-D Memoization (1336ms: 53.44%)
        memo = {}
        def helper(left, right, k):
            if left>right:
                return 0
            if (left, right, k) in memo:
                return memo[(left, right, k)]
            i = left+1
            while i<=right and boxes[i]==boxes[left]:
                i += 1
            res = (k+i-left)**2+helper(i, right, 0)
            for j in range(i, right+1):
                if boxes[j]==boxes[i-1]:
                    res = max(res, helper(i, j-1, 0)+helper(j, right, k+i-left))
            memo[(left, right, k)] = res
            return res
        return helper(0, len(boxes)-1, 0)