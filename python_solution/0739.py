class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # Solution 1: from Solution Using Stack (480ms: 88.64%)
        res = [0]*len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[i]>=T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1]-i
            stack.append(i)
        return res