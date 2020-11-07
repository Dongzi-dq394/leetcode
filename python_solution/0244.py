class WordDistance:

    def __init__(self, words: List[str]):
        self.dic = defaultdict(list)
        for i, word in enumerate(words):
            self.dic[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.dic[word1], self.dic[word2]
        s1 = s2 = 0
        res = float('Inf')
        while s1<len(l1) and s2<len(l2):
            res = min(res, abs(l1[s1]-l2[s2]))
            if l1[s1]<l2[s2]:
                s1 += 1
            else:
                s2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)