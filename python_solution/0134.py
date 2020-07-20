class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        have = [0] * len(gas)
        for i in range(len(gas)):
            have[i] = gas[i] - cost[i]
        if sum(have) < 0: return -1
        tank = res = 0
        for i in range(len(gas)):
            if tank + have[i] < 0:
                res = i+1
                tank = 0
            else:
                tank += have[i]
        return res