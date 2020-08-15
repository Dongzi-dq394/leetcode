class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Solution 1: DP (72ms: 83.55%%)
        if not dungeon or not dungeon[0]: return 0
        height, width = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = 1-min(0, dungeon[-1][-1])
        for i in range(width-2, -1, -1):
            dungeon[height-1][i] = max(1, dungeon[height-1][i+1]-dungeon[height-1][i])
        for i in range(height-2, -1, -1):
            dungeon[i][width-1] = max(1, dungeon[i+1][width-1]-dungeon[i][width-1])
        for i in range(height-2, -1, -1):
            for j in range(width-2, -1, -1):
                dungeon[i][j] = max(min(dungeon[i+1][j], dungeon[i][j+1])-dungeon[i][j], 1)
        return dungeon[0][0]