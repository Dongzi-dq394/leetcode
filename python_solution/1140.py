class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def helper(index, m):
            if index==len(piles):
                memo[(index, m)] = 0
                return 0
            if (index, m) in memo:
                return memo[(index, m)]
            pre_sum = 0
            temp = -float('Inf')
            for i in range(index, index+m*2):
                if i<len(piles):
                    pre_sum += piles[i]
                    if i+1<=index+m:
                        temp = max(temp, pre_sum-helper(i+1, m))
                    else:
                        temp = max(temp, pre_sum-helper(i+1, i+1-index))
            memo[(index, m)] = temp
            return temp
        return (sum(piles)+helper(0, 1))//2