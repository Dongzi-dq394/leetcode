class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Solution 1: from discussion --> LIS!! (160ms: 88.41%)
        # Very similar to the normal LIS problem
        # We need to sort the arr first and then binary search
        if not envelopes: return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for i in range(len(envelopes)):
            index = bisect.bisect_left(res, envelopes[i][1])
            if index==len(res):
                res.append(envelopes[i][1])
            else:
                res[index] = envelopes[i][1]
        return len(res)