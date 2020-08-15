class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # New Solution: Hash Table (48ms: 97.72%)
        count = Counter(nums) # one-pass
        res = 0
        # for-loop + while-loop is actually two-pass
        # still O(N) not O(N^2)
        for key in count:
            if key-1 not in count:
                temp = 1
                while key+1 in count:
                    temp += 1
                    key += 1
                res = max(res, temp)
        return res