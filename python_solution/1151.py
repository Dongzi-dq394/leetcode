class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Solution 1: Sliding Window (760ms: 51.97%)
        ones = sum(data)
        start = sum(data[:ones])
        res = ones-start
        for i in range(ones, len(data)):
            start += (data[i]-data[i-ones])
            res = min(res, ones-start)
        return res