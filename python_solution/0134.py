class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1
        for i in range(len(gas)):
            gas[i] -= cost[i]
        pre = 0 # The remaining gas, initialized to 0
        res = 0 # The result
        # Greedy, there must be one starting point.
        # If starting from one point, the remaining gas is always positive
        # then this point is where we should start.
        for i in range(len(gas)):
            if pre+gas[i]<0:
                res = i+1
                pre = 0
            else:
                pre += gas[i]
        return res