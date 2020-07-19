class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        ele = set(nums)
        for item in ele:
            if item-1 not in ele:
                cur = 1
                while item+1 in ele:
                    item += 1
                    cur += 1
                res = max(res, cur)
        return res