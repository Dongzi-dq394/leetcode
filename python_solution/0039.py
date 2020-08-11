class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # New Solution: Backtracking (80ms: 70%)
        res = []
        def backtracking(sub_res, cur_sum, index):
            if cur_sum == target:
                res.append(sub_res)
                return
            if cur_sum > target:
                return
            for i in range(index, len(candidates)):
                backtracking(sub_res+[candidates[i]], cur_sum+candidates[i], i)
        backtracking([], 0, 0)
        return res