class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # New Solution from discussion: Hash Table + Two Pointers (40ms: 78.52%)
        last_pos = {char: i for i, char in enumerate(S)}
        start = end = 0
        res = []
        for i, char in enumerate(S):
            end = max(end, last_pos[char])
            if i==end:
                res.append(end-start+1)
                start = end+1
        return res
        
        # New Solution by myself: Two Hash Tables (40ms: 78.52%)
        res = []
        freq = defaultdict(int)
        for char in S:
            freq[char] += 1
        start = 0
        dic = {}
        for i in range(len(S)):
            if S[i] not in dic:
                dic[S[i]] = True
            freq[S[i]] -= 1
            if freq[S[i]] == 0:
                dic.pop(S[i])
                if len(dic)==0:
                    res.append(i-start+1)
                    start = i+1
        return res