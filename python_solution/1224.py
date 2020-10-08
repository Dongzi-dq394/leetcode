class Leaderboard:
    
    # Solution by myself: Hash Table + Sorting (48ms: 98.01%)
    # Very simple... (I was thinking to use Heap or other method to store the scores...)

    def __init__(self):
        self.LB = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.LB:
            self.LB[playerId] = score
        else:
            self.LB[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(list(self.LB.values()))[-K:])

    def reset(self, playerId: int) -> None:
        self.LB.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)