class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # Solution: One-pass (60ms: 93.22%)
        ind1 = ind2 = None
        res = len(words)
        for i, word in enumerate(words):
            if word==word1:
                ind1 = i
                if ind2!=None:
                    res = min(res, abs(ind1-ind2))
            if word==word2:
                ind2 = i
                if ind1!=None:
                    res = min(res, abs(ind1-ind2))
        return res