class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # New Solution: Bit Manipulation (84ms: 91%)
        res = 0
        for i in nums:
            res ^= i
        return res