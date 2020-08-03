class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # Solution 1: from discussion (312ms: 67.56%) --> not like the normal 4Sum problem
        dic = {}
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                temp = A[i] + B[j]
                if temp not in dic:
                    dic[temp] = 1
                else:
                    dic[temp] += 1
        for i in range(len(C)):
            for j in range(len(D)):
                temp = - C[i] - D[j]
                if temp in dic:
                    res += dic[temp]
        return res
        
        # Solution 2: similar to the first solution, but very simple (284ms: 82.59%)
        count = Counter(a+b for a in A for b in B)
        return sum(count[-c-d] for c in C for d in D)