class Solution:
    def jump(self, nums: List[int]) -> int:
        # New Solution: DP / Greedy (92ms: 94.01%)
        res = 0
        pre_max = cur_max = 0
        for i, n in enumerate(nums):
            if i>pre_max:
                pre_max = cur_max
                res += 1
            cur_max = max(cur_max, i+n)
        return res