class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Solution 1: Normal DP (700ms: 30.68%)
        length = len(piles)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = piles[i]
        for j in range(1, length):
            for i in range(j-1, -1, -1):
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return True if dp[0][length-1]>0 else False
        
        # Solution 2: Pure Math!!
        # Very Smart, Alex can always win this game.
        return True