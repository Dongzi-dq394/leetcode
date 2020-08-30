class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Solution 1 from discussion: Memo + DP (764ms: 49.14%)
        # Something to learn:
        # we can hash a lot of things! we can transfer it to tuple/str
        memo = {}
        choice = [x for x in range(1, maxChoosableInteger+1)]
        if sum(choice)<desiredTotal:
            return False
        if sum(choice)==desiredTotal and maxChoosableInteger%2==1:
            return True
        def dfs(choice, remain):
            key = str(choice) # key = tuple(choice)
            if key in memo:
                return memo[key]
            if choice[-1]>=remain:
                memo[key] = True
                return True
            for i in range(len(choice)):
                if not dfs(choice[:i]+choice[i+1:], remain-choice[i]):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        # we can even pass the choice in tuple to save time
        return dfs(choice, desiredTotal)