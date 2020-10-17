class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        # Solution from Solution: Greedy (188ms: 70.80%)
        def transform(word, pre_len):
            if len(word)-pre_len-1<=1:
                return word
            return word[:pre_len]+str(len(word)-pre_len-1)+word[-1]
        res = []
        for word in dict:
            res.append(transform(word, 1))
        prefix = [1 for _ in range(len(dict))]
        for i in range(len(dict)-1):
            while True:
                same = set()
                for j in range(i+1, len(dict)):
                    if res[j]==res[i]:
                        same.add(j)
                if not same:
                    break
                same.add(i)
                for j in same:
                    prefix[j] += 1
                    res[j] = transform(dict[j], prefix[j])
        return res