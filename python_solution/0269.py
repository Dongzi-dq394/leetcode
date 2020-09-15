class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Solution 1: Topological Sort (32ms: 81.52%)
        if len(words)==1:
            return words[0]
        edges = defaultdict(list)
        degree = [0]*26
        dic = {}
        for word in words:
            for char in word:
                dic[char] = True
        for i in range(len(words)-1):
            big, small = words[i], words[i+1]
            length = min(len(big), len(small))
            j = 0
            while j<length and big[j]==small[j]:
                j += 1
            if j!=length:
                edges[big[j]].append(small[j])
                degree[ord(small[j])-97] += 1
            else:
                if len(big)>len(small):
                    return ''
        distinct_num = len(dic)
        zero = []
        for i in range(26):
            if degree[i]==0 and chr(i+97) in dic:
                zero.append(chr(i+97))
        res = []
        while zero:
            node = zero.pop(0)
            res.append(node)
            for vertice in edges[node]:
                degree[ord(vertice)-97] -= 1
                if degree[ord(vertice)-97] == 0:
                    zero.append(vertice)
        return ''.join(res) if len(res)==distinct_num else ''