class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = defaultdict(int)
        for x, y, z in transactions:
            debt[x] -= z
            debt[y] += z
        ele = []
        for key in debt:
            if debt[key]!=0:
                ele.append(debt[key])
        def helper(index):
            while index<len(ele) and ele[index]==0:
                index += 1
            if index==len(ele):
                return 0
            res = float('Inf')
            for i in range(index+1, len(ele)):
                if ele[i]*ele[index]<0:
                    ele[i] += ele[index]
                    res = min(res, 1+helper(index+1))
                    ele[i] -= ele[index]
            return res if res!=float('Inf') else 0
        return helper(0)