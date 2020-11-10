class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # Solution 1: Pure Backtracking (TLE!!)
        res = []
        length = len(words[0])
        def backtracking(sub_res, remain, ind):
            if ind==length:
                res.append(sub_res)
                return
            elements = remain[ind]
            string = ''.join(item for item in elements)
            for i in range(len(words)):
                if words[i][:ind]==string:
                    for j in range(ind+1, length):
                        remain[j].append(words[i][j])
                    backtracking(sub_res+[words[i]], remain, ind+1)
                    for j in range(ind+1, length):
                        remain[j].pop()
            return
        for i in range(len(words)):
            remain = [[item] for item in words[i]]
            backtracking([words[i]], remain, 1)
        return res
        
        # Solution 2 with some hints: Hash Table + Backtracking (588ms: 20.37%)
        # We can also use Trie but store the word in each level.
        res = []
        length = len(words[0])
        dic = defaultdict(list)
        for word in words:
            for i in range(length):
                dic[word[:i+1]].append(word)
        def backtracking(sub_res, remain, ind):
            if ind==length:
                res.append(sub_res)
                return
            string = ''.join(item for item in remain[ind])
            for word in dic[string]:
                for i in range(ind+1, length):
                    remain[i].append(word[i])
                backtracking(sub_res+[word], remain, ind+1)
                for i in range(ind+1, length):
                    remain[i].pop()
            return
        for word in words:
            backtracking([word], [[item] for item in word], 1)
        return res