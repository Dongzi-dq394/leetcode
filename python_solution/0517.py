class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sum_val = sum(machines)
        if sum_val%len(machines)!=0:
            return -1
        target = sum_val//len(machines)
        start = 0
        res = 0
        for num in machines:
            start += num-target
            res = max(res, abs(start), num-target)
        return res