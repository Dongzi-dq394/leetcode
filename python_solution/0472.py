class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Solution 1: Memoization (432ms: 76.41%)
        dic = {word: True for word in words}
        res = []
        memo = {}
        def checker(string):
            if string in memo:
                return memo[string]
            memo[string] = False
            for i in range(1, len(string)):
                first, second = string[:i], string[i:]
                if first in dic and second in dic:
                    memo[string] = True
                    return True
                if first in dic and checker(second):
                    memo[string] = True
                    return True
            return False
        for word in words:
            if checker(word):
                res.append(word)
        return res