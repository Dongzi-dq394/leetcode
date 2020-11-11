class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # Solution 1: Backtracking (24ms: 98.14%)
        count = Counter(s)
        if sum(1 for item in count if count[item]%2==1)>1: return []
        mid = ''
        length = len(s)//2
        res = []
        for key in count:
            if count[key]%2==1:
                mid = key
                break
        def backtracking(sub_res):
            if len(sub_res)==length:
                res.append(sub_res+mid+sub_res[::-1])
                return
            for key in count:
                if count[key]>1:
                    count[key] -= 2
                    backtracking(sub_res+key)
                    count[key] += 2
            return
        backtracking('')
        return list(set(res))